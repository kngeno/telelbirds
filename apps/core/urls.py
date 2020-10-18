from django.conf.urls import patterns, url

from .views import HelpPageView, MailingListSignupAjaxView


urlpatterns = patterns('',
    url(
        regex=r'^help/',
        view=HelpPageView.as_view(),
        name='help',
    ),
    url(
        regex=r'^mailing-list-signup-ajax-view/',
        view=MailingListSignupAjaxView.as_view(),
        name='mailing_list_signup_ajax_view',
    ),
)
