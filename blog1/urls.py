"""blog1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from raulchirinos.models import Post
from raulchirinos.views import Archive

app_name = 'raulchirinos'
urlpatterns = [
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^admin/', admin.site.urls, name='admin-site'),
    url(r'^$', ListView.as_view(model=Post, template_name='raulchirinos/index.html'), name='index'),
    url(r'^post/(?P<slug>[\w-]+)/$', DetailView.as_view(model=Post, template_name='raulchirinos/post_template/post.html'), name='post_details'),
    url(r'^archive/$', Archive.as_view(template_name='raulchirinos/archive.html'), name='Archive')
]
