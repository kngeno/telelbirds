from django.views.generic.base import ContextMixin
from django.views.generic import DetailView, ListView

from taggit.models import TaggedItem

from .models import Blog, BlogAd


class BlogBaseView(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(BlogBaseView, self).get_context_data(**kwargs)
        context['blog_tags'] = TaggedItem.tags_for(Blog).order_by('name')
        context['recent_blog_list'] = Blog.objects.recent_posts()

        return context


class BlogDetailView(DetailView, BlogBaseView):
    model = Blog

    def get_queryset(self):
        """
        Only return the object if it's public, unless the user is a superuser.
        """
        if self.request.user.is_authenticated() and \
                self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.publicly_viewable()

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['ad_top'] = BlogAd.objects.filter(position=BlogAd.TOP)\
            .order_by('?').first()
        context['ad_middle'] = BlogAd.objects.filter(position=BlogAd.MIDDLE)\
            .order_by('?').first()
        context['ad_bottom'] = BlogAd.objects.filter(position=BlogAd.BOTTOM)\
            .order_by('?').first()

        return context


class BlogListView(ListView, BlogBaseView):
    model = Blog
    paginate_by = 15

    def get_queryset(self):
        """
        Only return public blog posts.
        """
        return Blog.objects.publicly_viewable()


class BlogTagListView(BlogListView):
    """
    Display a Blog List page filtered by tag.
    """

    def get_queryset(self):
        result = super(BlogTagListView, self).get_queryset()
        return result.filter(tags__name=self.kwargs.get('tag'))
