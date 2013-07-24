# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import Group
from menu.models import Item
from menu.models import GroupAttribute
from menu.models import ItemAttribute
# translation
# from modeltranslation.admin import TranslationAdmin


class GroupAttributeInline(admin.StackedInline):
	model = GroupAttribute
	extra = 0


class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'public', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	list_editable = ['public']
	list_filter = ['public']
	inlines = [GroupAttributeInline]

admin.site.register(Group, GroupAdmin)


class ItemAttributeInline(admin.StackedInline):
	model = ItemAttribute
	extra = 0


class ItemAdmin(admin.ModelAdmin):
	list_display = ('display', 'get_absolute_url', 'group', 'sort', 'public', 'url_type', 'access', 'icon_preview')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('sort',)
	list_filter = ('public', 'group', 'access', 'sites')
	inlines = [ItemAttributeInline]

	# class Media:
		# js = (
			# 'modeltranslation/js/force_jquery.js',
			# 'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
			# 'modeltranslation/js/tabbed_translation_fields.js',
		# )
		# css = {
			# 'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		# }

admin.site.register(Item, ItemAdmin)
