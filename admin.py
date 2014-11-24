from django.contrib import admin
from django.contrib.sites.models import Site 
from django.contrib.contenttypes.models import ContentType


from .models import Group
from .models import Item


def site_unicode(self): 
	return self.name 

Site.__unicode__ = site_unicode


def contenttype_unicode(self): 
	return '%s -> %s' % (self.app_label, self.name)

ContentType._meta.ordering = ['app_label', 'name']
ContentType.__unicode__ = contenttype_unicode


class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'description', 'public', 'menu', 'count')
	search_fields = ('name', 'slug', 'description', 'id')
	list_editable = ['public']
	list_filter = ['public']

admin.site.register(Group, GroupAdmin)


class ItemAdmin(admin.ModelAdmin):
	list_display = ['display', 'get_absolute_url', 'group', 'sort', 'public', 'icon_preview']
	search_fields = ['name', 'url', 'group']
	list_editable = ['sort', 'public']
	list_filter = ['public', 'group', 'access', 'sites']
	actions = ['update']

	def update(self, request, queryset):
		for item in Item.objects.all():
			item.sort = 11
			item.save()
		self.message_user(request, "Updated")
	update.short_description = "Update selected menu"


admin.site.register(Item, ItemAdmin)
