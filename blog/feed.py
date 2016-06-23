from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from .models import Post

class LatestPost(Feed):
    title = "Latests posts"
    link = "/"
    def items(self):
        return Post.objects.all()[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return '/rss/'