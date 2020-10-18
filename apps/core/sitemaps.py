from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = 'daily'

    def items(self):
        return ['home', 'signup', 'login']

    def location(self, item):
        return reverse(item)