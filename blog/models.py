#coding: utf-8
from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, verbose_name='SEO URL')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
