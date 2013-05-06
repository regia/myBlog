#!/usr/bin/env python
# -*-coding: UTF-8 -*-

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import Post


class BlogFeed(Feed):
    title = "Regedi's blog feed"
    link = "/feed/"
    description = "Updates on changes and additions to regedi's blog."

    def items(self):
        return Post.objects.order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        date = item.created
        year = date.year
        month = date.month
        if len(str(month)) < 2:
            month = "0" + str(month)
        return reverse('blog.views.post', args=[year, month, item.slug])
