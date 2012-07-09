# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import *

class MenuGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	
admin.site.register(MenuGroup, MenuGroupAdmin)

class MenuAdmin(admin.ModelAdmin):
	list_display = ('display', 'get_absolute_url', 'group', 'sort', 'public', 'url_type', 'icon_preview')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('public', 'sort')
	list_filter = ('group', 'public')

admin.site.register(Menu, MenuAdmin)