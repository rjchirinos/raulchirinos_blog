# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_markdown.models import MarkdownField


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=2000000)
    tags = models.ManyToManyField(Tag)
    author = models.CharField(max_length=255, default='Raúl Chirinos')
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
