# -*- coding: utf-8 -*
from django.contrib import admin
from menu.models import Group
from menu.models import Item
# translation
# from modeltranslation.admin import TranslationAdmin



class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'public', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	list_editable = ['public']
	list_filter = ['public']

admin.site.register(Group, GroupAdmin)


from django.conf.urls import patterns
from django.shortcuts import render_to_response

from django.template import RequestContext


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



	def get_urls(self):
		urls = super(ItemAdmin, self).get_urls()
		my_urls = patterns('',
			(r'^update/$', self.admin_site.admin_view(self.update))
		)
		return my_urls + urls

	def update(self, request):
		context = {}
		return render_to_response('menu/update.html', context, context_instance=RequestContext(request), mimetype='text/plain')




admin.site.register(Item, ItemAdmin)


def your_action(self, request, queryset):
	pass


admin.site.add_action(your_action)
