#coding: utf-8
from django.contrib import admin
from blog.models import Post
from blog.models import Profile


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'description', 'created', 'modified')

    # class Media:
    #     css = {
    #         'all' : ('/static/css/monokai.css',)
    #     }
    #     js = ('/static/js/highlight.pack.js',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'userpic')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)