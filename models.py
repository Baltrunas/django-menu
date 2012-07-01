# -*- coding: utf-8 -*
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

from django.contrib.sites.models import Site

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class MenuGroup(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))
	text = models.TextField(verbose_name=_('Text'), blank=True)
	sites = models.ManyToManyField(Site, related_name='menus', verbose_name=_('Sites'), null=True, blank=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)
	
	def menu(self):
		return '<a href="../menu/?group__id__exact=%s"><img src="%smenu_item_list.png"></a>' % (self.id, str(settings.STATIC_URL))
	menu.short_description = _('Menu')
	menu.allow_tags = True

	def count(self):
		return Menu.objects.filter(group=self.id).count()
	count.short_description = _('Count')

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _('Menu Group')
		verbose_name_plural = _('Menu Groups')

class Menu(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	URL_TYPE_CHOICES = (
		('internal', _('internal')),
		('external', _('external')),
	)
	url_type = models.CharField(verbose_name=_('URL Type'), max_length=10, choices=URL_TYPE_CHOICES)
	url = models.CharField(verbose_name=_('URL'), max_length=255, default='#')
	content_type = models.ForeignKey(ContentType, verbose_name=_('Content Type'), null=True, blank=True)
	object_id = models.PositiveIntegerField(verbose_name=_('Object ID'), null=True, blank=True)
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	
	order = models.SlugField(verbose_name=_('Order'), max_length=255, editable=False)
	
	group = models.ForeignKey(MenuGroup, verbose_name=_('Menu Group'))
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	icon = models.ImageField(verbose_name=_('Icon'), upload_to='img/menu', blank=True)
	text = models.TextField(verbose_name=_('Text'), blank=True)
	sort = models.PositiveSmallIntegerField(verbose_name=_('Sort'), default=500)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)
	
	def get_absolute_url(self):
		if self.url_type == 'internal':
			if hasattr(self.content_object, 'get_absolute_url'):
				if type(self.content_object.get_absolute_url).__name__ == 'instancemethod':
					return self.content_object.get_absolute_url()
				elif type(self.content_object.get_absolute_url).__name__ == 'str':
					return self.content_object.get_absolute_url
				else:
					return '#'
			else:
				return '#'
		else:
			return self.url
	
	def icon_preview(self):
		if self.icon:
			return '<img src="%s">' % self.icon.url
		else:
			return '(none)'
	icon_preview.short_description = _('Icon')
	icon_preview.allow_tags = True

	def order_puth (self, id):
		this = Menu.objects.get(pk=id)
		puth = str(this.sort) + ':' + this.name.replace('|', '')
		if this.parent:
			return self.order_puth(Menu.objects.get(pk=this.parent.id).id) + '|' + puth
		else:
			return puth

	def save(self, *args, **kwargs):
		super(Menu, self).save(*args, **kwargs)
		self.order = self.order_puth(self.id)
		super(Menu, self).save(*args, **kwargs)
		for item in Menu.objects.filter(parent = self.id):
			item.save()

	def display(self):
		return '&nbsp;' * (len(self.order.split('|')) -1) * 8 + self.name
	display.short_description = _('Menu')
	display.allow_tags = True


	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['order', 'sort', 'name']
		verbose_name = _('Menu')
		verbose_name_plural = _('Menus')