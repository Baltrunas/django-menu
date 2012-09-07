# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import *

class MenuGroupOptionInline(admin.StackedInline):
	model = MenuGroupOption
	extra = 0

class MenuGroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	inlines = [MenuGroupOptionInline]
	
admin.site.register(MenuGroup, MenuGroupAdmin)

class MenuOptionInline(admin.StackedInline):
	model = MenuOption
	extra = 0

class MenuAdmin(admin.ModelAdmin):
	list_display = ('display', 'get_absolute_url', 'group', 'sort', 'public', 'url_type', 'icon_preview')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('public', 'sort')
	list_filter = ('group', 'public')
	inlines = [MenuOptionInline]

admin.site.register(Menu, MenuAdmin)


# class MenuOptionAdmin(admin.ModelAdmin):
# 	list_display = ('place', 'name', 'value')
# 	search_fields = ('place', 'name', 'value')
	
# admin.site.register(MenuOption, MenuOptionAdmin)