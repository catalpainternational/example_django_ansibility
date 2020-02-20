"""CattlePainterNational URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from paintjobs import views as pjviews

urlpatterns = [
    url(r'^$', pjviews.index, name='index'),
    url(r'^raise$', pjviews.raise_e, name='raise'),
    url(r'^stdout$', pjviews.shoutstdout, name='stdout'),
    url(r'^stderr$', pjviews.shoutstderr, name='stderr'),
    url(r'^oom$', pjviews.oom, name='oom'),
    url(r'^oom/(?P<mb>[0-9]+)$', pjviews.oom, name='oom'),
    url(r'^faffing$', pjviews.faffing, name='faffing'),
    url(r'^faffing/(?P<duration>[0-9]+)$', pjviews.faffing, name='faffing'),
    url(r'^testcache$', pjviews.testcache, name='testcache'),
    url(r'^whatscheme$', pjviews.whatscheme, name='whatscheme'),
    url(r'^browserquotum$', pjviews.browserquotum, name='browserquotum'),
    url(r'^admin/', include(admin.site.urls)),
]
