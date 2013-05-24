#!/usr/bin/env python
# -*-coding: UTF-8 -*-
from models import Post
from django.forms import ModelForm


class AddPostForm(ModelForm):
    class Meta:
        model = Post

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas_frontend.js')