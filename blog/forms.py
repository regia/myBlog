#!/usr/bin/env python
# -*-coding: UTF-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Post, Profile
from django.forms import ModelForm


class AddPostForm(ModelForm):
    class Meta:
        model = Post

    # class Media:
    #     js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/tiny_mce/textareas_frontend.js')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ("username", "email",)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(ModelForm):
    class Meta:
        model = Profile