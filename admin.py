# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import *

class MenuGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'text', 'menu', 'count')
	search_fields = ('name', 'slug', 'text', 'id')
	
admin.site.register(MenuGroup, MenuGroupAdmin)

class MenuAdmin(admin.ModelAdmin):
	list_display = ('display', 'url', 'group', 'sort', 'public', 'icon_preview', 'url_type', 'order')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('public', 'sort')
	list_filter = ('group', 'public')

admin.site.register(Menu, MenuAdmin)