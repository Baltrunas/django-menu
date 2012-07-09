# -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url

urlpatterns = patterns('menu.views',
    url(r'^url_patterns/$', 'url_patterns', name='menu_url_patterns'),
    url(r'^tree/(?P<group_id>\d)/(?P<id>\d)/$', 'tree', name='menu_tree'),
)
