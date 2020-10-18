from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.text import Truncator

from blogs.models import Blog


class LatestBlogsFeed(Feed):
    site_name = settings.SITE_NAME
    title = 'Simple Glucose Management App | %s' % site_name
    link = '/'
    description = 'Updates on changes and additions to %s' % site_name

    def items(self):
        return Blog.objects.recent_posts()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return Truncator(item.content).words(75)