import logging

from django.views.generic import TemplateView, FormView, View
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

import mailchimp
from braces.views import (
    AjaxResponseMixin,
    JSONResponseMixin,
    LoginRequiredMixin,
)

from glucoses.models import Glucose

from .forms import ContactForm


logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['glucose_count'] = Glucose.objects.count()

        return context


class HelpPageView(LoginRequiredMixin, FormView):
    success_url = '.'
    form_class = ContactForm
    template_name = 'core/help.html'

    def get_initial(self):
        return {
            'email': self.request.user.email
        }

    def form_valid(self, form):
        success_message = '''Email sent! We'll try to get back to you as
            soon as possible.'''
        messages.add_message(self.request, messages.SUCCESS, success_message)

        return super(HelpPageView, self).form_valid(form)

    def form_invalid(self, form):
        failure_message = 'Email not sent. Please try again.'
        messages.add_message(self.request, messages.WARNING, failure_message)

        return super(HelpPageView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            support_email = settings.CONTACTS['support_email']

            message = 'Sent By: %s (%s)\n\n%s' % (
                form.cleaned_data['email'],
                self.request.user.username,
                form.cleaned_data['message'])

            email = EmailMessage(
                from_email=support_email,
                subject='[Help] %s ' % form.cleaned_data['subject'],
                body=message,
                to=[support_email])

            email.send()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class MailingListSignupAjaxView(JSONResponseMixin, AjaxResponseMixin, View):
    """
    Sign up an email address to a MailChimp list.
    """

    def post_ajax(self, request, *args, **kwargs):
        email = request.POST.get('email').strip().lower()
        mailchimp_list_id = settings.MAILCHIMP_LIST_ID

        response_dict = {
            'message': '{0} successfully subscribed to {1}!'.format(
                email, mailchimp_list_id),
        }

        mc = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)

        try:
            mc.lists.subscribe(
                id=mailchimp_list_id,
                email={'email': email},
                update_existing=True,
                double_optin=True,
            )
            logger.info('%s successfully subscribed to %s', email,
                        mailchimp_list_id)
        except mailchimp.Error, e:
            logger.error('A MailChimp error occurred: %s', e)

            response_dict['message'] = 'Sorry, an error occurred.'
            return self.render_json_response(response_dict, status=500)

        return self.render_json_response(response_dict)