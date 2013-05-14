#coding: utf-8
from django.contrib import admin
from blog.models import Post
from blog.models import Profile


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'description', 'created', 'modified')

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas.js',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'userpic')

admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)