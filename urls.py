# -*- coding: utf-8 -*
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('menu.views',
	# Update
	url(r'^update/$', 'update', name='menu_update'),

	# URL to load url patterns for adding menu items
	url(r'^url_patterns/$', 'url_patterns', name='menu_url_patterns'),
	# Perens tree for menu item
	url(r'^parent_tree/(?P<group_id>\d+)/(?P<id>\d+)/$', 'parent_tree', name='menu_parent_tree'),
	# Perents tree url patterns template to replace in change form by ajax
	url(r'^parent_tree/group_id/original_id/$', 'parent_tree', name='menu_parent_tree_url_pattern'),
)
