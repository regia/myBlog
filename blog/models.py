#coding: utf-8
from django.db import models
#from django.db.models.signals import post_save
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from fields import AutoOneToOneField
from PIL import Image
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    slug = models.SlugField(unique=True, verbose_name='SEO URL')
    description = RichTextField(verbose_name="Description")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    count_visited = models.IntegerField()
    tags = TaggableManager(verbose_name="Tags")

    def __unicode__(self):
        return self.title


class Profile(models.Model):
    user = AutoOneToOneField(User, related_name='profile', verbose_name='User', primary_key=True)
    userpic = models.ImageField(upload_to="userpics/", max_length=500)
    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title

    def save(self):

        if not self.userpic:
            return

        super(Profile, self).save()

        image = Image.open(self.userpic)
        if image.size[0]< 150:
            size = image.size
        else:
            size = (150, 150)
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(self.userpic.path)


# def user_post_save(sender, instance, *args, **kwargs):
#     # Creates user profile
#     profile, new = Profile.objects.get_or_create(user=instance)
#
# post_save.connect(user_post_save, User)
