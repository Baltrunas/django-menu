# -*- coding: utf-8 -*
# ugettext_lazy for translation
from django.utils.translation import ugettext_lazy as _
# import the settings file
from django.conf import settings
# sites for menu group
from django.contrib.sites.models import Site
# contenttypes for menu to create urls to object of model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
# for access control
from django.contrib.auth import models as Auth
# django ORM
from django.db import models


if 'hvad' in settings.INSTALLED_APPS and 'LANGUAGES' in settings:
	from hvad.models import TranslatableModel, TranslatedFields
	TranslatableModel = TranslatableModel
else:
	TranslatableModel = models.Model


class Group (models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))
	description = models.TextField(verbose_name=_('Description'), blank=True)
	sites = models.ManyToManyField(Site, verbose_name=_('Sites'), related_name='menus', null=True, blank=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	# Link to items of this group
	def menu(self):
		return '<a href="../item/?group__id__exact=%s"><img src="%simg/menu/item_list.png"></a>' % (self.id, str(settings.STATIC_URL))
	menu.short_description = _('Menu')
	menu.allow_tags = True

	# Count of items in this group
	def count(self):
		return self.items.count()
	count.short_description = _('Count')

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']
		verbose_name = _('Menu Group')
		verbose_name_plural = _('Menu Groups')


class Item (TranslatableModel):
	if hvad:
		translations = TranslatedFields(
			name=models.CharField(verbose_name=_('Name'), max_length=255),
			description=models.TextField(verbose_name=_('Description'), blank=True)
		)
	else:
		name = models.CharField(verbose_name=_('Name'), max_length=255)
		description = models.TextField(verbose_name=_('Description'), blank=True)

	URL_TYPE_CHOICES = (
		(_('internal'),
			(
				('model-oblect', _('model oblect')),
				('url-patterns', _('url patterns')),
			)
		),
		(_('external'),
			(
				('external', _('external')),
			)
		),
	)
	url_type = models.CharField(verbose_name=_('URL Type'), max_length=20, choices=URL_TYPE_CHOICES)
	# for external url
	url = models.CharField(verbose_name=_('URL'), max_length=255, default='#', blank=True)
	# for model object
	content_type = models.ForeignKey(ContentType, verbose_name=_('Content Type'), null=True, blank=True)
	object_id = models.PositiveIntegerField(verbose_name=_('Object ID'), null=True, blank=True)
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	# for url patterns
	url_patterns = models.CharField(verbose_name=_('url patterns'), max_length=255, blank=True)
	url_options = models.TextField(verbose_name=_('URL Options'), blank=True, help_text='key1=value1<br>key2=value2')

	group = models.ForeignKey(Group, related_name='items', verbose_name=_('Menu Group'))
	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	icon = models.ImageField(verbose_name=_('Icon'), upload_to='img/menu', blank=True)

	sort = models.PositiveSmallIntegerField(verbose_name=_('Sort'), default=500)
	order = models.SlugField(verbose_name=_('Order'), max_length=255, editable=False)

	ACCESS_CHOICES = (
		('all', _('All')),
		('anonymous_only', _('Anonymous only')),
		('login_required', _('Login required')),
		('exclude', _('Except')),
		('filter', _('Only')),
		('advanced_access', _('Advanced Access')),
	)
	access = models.CharField(verbose_name=_('Access'), max_length=32, choices=ACCESS_CHOICES, default='all')
	access_group = models.ManyToManyField(Auth.Group, verbose_name=_('Access Group'), related_name='menus', null=True, blank=True)
	access_user = models.ManyToManyField(Auth.User, verbose_name=_('Access User'), related_name='menus', null=True, blank=True)

	BOOL_CHOICES = (
		(0, _('All')),
		(1, _('Yes')),
		(2, _('No')),
	)

	access_is_active = models.PositiveSmallIntegerField(verbose_name=_('Is active'), max_length=1, choices=BOOL_CHOICES, default=0)
	access_is_staff = models.PositiveSmallIntegerField(verbose_name=_('Is staff'), max_length=1, choices=BOOL_CHOICES, default=0)
	access_is_superuser = models.PositiveSmallIntegerField(verbose_name=_('Is superuser'), max_length=1, choices=BOOL_CHOICES, default=0)

	access_denied_group = models.ManyToManyField(Auth.Group, verbose_name=_('Denied Group'), related_name='denied_menus', null=True, blank=True)
	access_denied_user = models.ManyToManyField(Auth.User, verbose_name=_('Denied User'), related_name='denied_menus', null=True, blank=True)

	access_denied_is_active = models.PositiveSmallIntegerField(verbose_name=_('Is active'), max_length=1, choices=BOOL_CHOICES, default=0)
	access_denied_is_staff = models.PositiveSmallIntegerField(verbose_name=_('Is staff'), max_length=1, choices=BOOL_CHOICES, default=0)
	access_denied_is_superuser = models.PositiveSmallIntegerField(verbose_name=_('Is superuser'), max_length=1, choices=BOOL_CHOICES, default=0)

	level = models.PositiveSmallIntegerField(verbose_name=_('Level'), default=0, editable=False)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	@models.permalink
	def create_url(self):
		options = {}
		for option in self.url_options.split('\n'):
			if option:
				option = option.split('=')
				options[option[0]] = option[1]
		return (self.url_patterns, (), options)

	def get_absolute_url(self):
		if self.url_type == 'model-oblect':
			if hasattr(self.content_object, 'get_absolute_url'):
				if type(self.content_object.get_absolute_url).__name__ == 'instancemethod':
					return self.content_object.get_absolute_url()
				elif type(self.content_object.get_absolute_url).__name__ == 'str':
					return self.content_object.get_absolute_url
				else:
					return '#'
			else:
				return '#'
		if self.url_type == 'url-patterns':
			return self.create_url()
		else:
			return self.url

	def icon_preview(self):
		if self.icon:
			return '<img src="%s">' % self.icon.url
		else:
			return '(none)'
	icon_preview.short_description = _('Icon')
	icon_preview.allow_tags = True

	def order_puth(self, this):
		puth = str(this.sort) + ':' + str(this.pk)
		# puth = str(this.sort) + ':' + this.name.replace('|', '')
		if this.parent:
			return self.order_puth(this.parent) + '|' + puth
		else:
			return puth

	def save(self, *args, **kwargs):
		obj = super(Item, self).save(*args, **kwargs)
		self.order = self.order_puth(self)
		self.level = len(self.order.split('|')) - 1
		if self.parent:
			self.group = self.parent.group
		super(Item, self).save(*args, **kwargs)
		for item in self.childs.all():
			item.save()
		return obj

	def is_current(self, url):
		self_url = self.get_absolute_url()
		if self_url == url:
			return 'current'
		elif self_url != '/' and self_url in url:
			return 'parent_of_current'
		return ''

	def display(self):
		return '&nbsp;' * self.level * 8 + self.name
	display.short_description = _('Menu')
	display.allow_tags = True

	def __unicode__(self, *args, **kwargs):
		if hvad:
			return self.safe_translation_getter('name', 'MyMode: %s' % self.pk)
		else:
			return self.name

	class Meta:
		ordering = ['order', 'sort']
		verbose_name = _('Menu')
		verbose_name_plural = _('Menus')


class GroupAttribute(models.Model):
	group = models.ForeignKey(Group, verbose_name=_('Menu Group'), related_name='options')
	PLACE_CHOICES = (
		('ul', 'ul'),
		('li', 'li'),
		('a', 'a'),
		('anchor', _('Anchor')),
	)
	place = models.CharField(max_length=20, choices=PLACE_CHOICES)
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	value = models.CharField(verbose_name=_('Value'), max_length=256)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name + '=' + self.value

	class Meta:
		ordering = ['name']
		verbose_name = _('Menu Group Option')
		verbose_name_plural = _('Menu Group Options')


class ItemAttribute (models.Model):
	item = models.ForeignKey(Item, verbose_name=_('Menu Item'), related_name='options')
	PLACE_CHOICES = (
		('ul', 'ul'),
		('li', 'li'),
		('a', 'a'),
		('anchor', _('Anchor')),
	)
	place = models.CharField(max_length=20, choices=PLACE_CHOICES)
	name = models.CharField(verbose_name=_('Name'), max_length=256)
	value = models.CharField(verbose_name=_('Value'), max_length=256)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def __unicode__(self):
		return self.name + '=' + self.value

	class Meta:
		ordering = ['name']
		verbose_name = _('Menu Option')
		verbose_name_plural = _('Menu Options')
