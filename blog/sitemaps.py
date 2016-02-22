#==========| M4N6L0 | ==========#
#                               #
#==========| M4N6L0 | ==========#

from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def item(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish