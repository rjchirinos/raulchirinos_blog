# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms

from .models import Post, Tag

admin.site.register(Post)
admin.site.register(Tag)
