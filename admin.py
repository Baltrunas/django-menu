# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import *

class MenuGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'text', 'menu', 'count')
	search_fields = ('name', 'slug', 'text', 'id')
	# class Media:
		# js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)
admin.site.register(MenuGroup, MenuGroupAdmin)

class MenuAdmin(admin.ModelAdmin):
	list_display = ('display', 'url', 'group', 'sort', 'public', 'icon_preview', 'order')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('public', 'sort')
	list_filter = ('group', 'public')
	# class Media:
		# js = ('tiny_mce/tiny_mce.js', 'tiny_mce/textareas.js',)

admin.site.register(Menu, MenuAdmin)