# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import *

class GroupAttributeInline(admin.StackedInline):
	model = GroupAttribute
	extra = 0

class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	inlines = [GroupAttributeInline]

admin.site.register(Group, GroupAdmin)

class ItemAttributeInline(admin.StackedInline):
	model = ItemAttribute
	extra = 0

class ItemAdmin(admin.ModelAdmin):
	list_display = ('display', 'get_absolute_url', 'group', 'sort', 'public', 'url_type', 'icon_preview')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('public', 'sort')
	list_filter = ('group', 'public')
	inlines = [ItemAttributeInline]

admin.site.register(Item, ItemAdmin)


# class MenuOptionAdmin(admin.ModelAdmin):
# 	list_display = ('place', 'name', 'value')
# 	search_fields = ('place', 'name', 'value')
	
# admin.site.register(MenuOption, MenuOptionAdmin)