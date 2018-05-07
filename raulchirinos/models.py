# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = MarkdownxField()
    tags = models.ManyToManyField(Tag)
    author = models.CharField(max_length=255, default='Raúl Chirinos')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True)

    class Meta:
        ordering = ['-date']

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
