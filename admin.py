# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import Group
from menu.models import Item
# translation
# from modeltranslation.admin import TranslationAdmin


from django.contrib.sites.models import Site 
def __unicode__(self): 
	return self.name 

Site.__unicode__ = __unicode__

from django.contrib.contenttypes.models import ContentType
def __unicode__(self): 
	return '%s -> %s' % (self.app_label, self.name)


ContentType._meta.ordering = ['app_label', 'name']
ContentType.__unicode__ = __unicode__



class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'public', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	list_editable = ['public']
	list_filter = ['public']

admin.site.register(Group, GroupAdmin)


class ItemAdmin(admin.ModelAdmin):
	list_display = ('display', 'get_absolute_url', 'group', 'sort', 'public', 'url_type', 'access', 'icon_preview')
	search_fields = ('name', 'url', 'group', 'sort', 'public')
	list_editable = ('sort',)
	list_filter = ('public', 'group', 'access', 'sites')

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
