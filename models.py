from django.utils.translation import ugettext_lazy as _

from django.conf import settings

from django.contrib.sites.models import Site

from django.contrib.auth import models as Auth

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.db import models


class Group (models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=128)
	slug = models.SlugField(verbose_name=_('Slug'), max_length=128, help_text=_('A slug is the part of a URL which identifies a page using human-readable keywords'))

	sites = models.ManyToManyField(Site, verbose_name=_('Sites'), related_name='menus', blank=True)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	# Link to items of this group
	def menu(self):
		return '<a href="../item/?group__id__exact=%s"><img src="%smenu/img/item_list.png"></a>' % (self.id, str(settings.STATIC_URL))
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


class Item (models.Model):
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
	content_object = GenericForeignKey('content_type', 'object_id')
	# for url patterns
	url_patterns = models.CharField(verbose_name=_('url patterns'), max_length=255, blank=True)
	url_options = models.TextField(verbose_name=_('URL Options'), blank=True, help_text='key1=value1<br>key2=value2')

	group = models.ForeignKey(Group, related_name='items', verbose_name=_('Menu Group'))

	parent = models.ForeignKey('self', verbose_name=_('Parent'), null=True, blank=True, related_name='childs')
	level = models.PositiveSmallIntegerField(verbose_name=_('Level'), null=True, blank=True, editable=False, default=0)
	childs_count = models.PositiveIntegerField(verbose_name=_('Childs Count'), null=True, blank=True, editable=False)

	left_key = models.PositiveIntegerField(verbose_name=_('Left Key'), null=True, blank=True, editable=False)
	right_key = models.PositiveIntegerField(verbose_name=_('Right Key'), null=True, blank=True, editable=False)

	order = models.SlugField(verbose_name=_('Order'), max_length=255, editable=False)

	sort = models.PositiveSmallIntegerField(verbose_name=_('Sort'), default=500)

	icon = models.ImageField(verbose_name=_('Icon'), upload_to='img/menu', blank=True)

	ACCESS_CHOICES = (
		('all', _('All')),
		('anonymous_only', _('Anonymous only')),
		('login_required', _('Login required')),
		('exclude', _('Except')),
		('filter', _('Only')),
		('advanced_access', _('Advanced Access')),
	)
	access = models.CharField(verbose_name=_('Access'), max_length=32, choices=ACCESS_CHOICES, default='all')
	access_group = models.ManyToManyField(Auth.Group, verbose_name=_('Access Group'), related_name='menus', blank=True)
	access_user = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('Access User'), related_name='menus', blank=True)

	BOOL_CHOICES = (
		(0, _('All')),
		(1, _('Yes')),
		(2, _('No')),
	)

	access_is_active = models.PositiveSmallIntegerField(verbose_name=_('Is active'), choices=BOOL_CHOICES, default=0)
	access_is_staff = models.PositiveSmallIntegerField(verbose_name=_('Is staff'), choices=BOOL_CHOICES, default=0)
	access_is_superuser = models.PositiveSmallIntegerField(verbose_name=_('Is superuser'), choices=BOOL_CHOICES, default=0)

	access_denied_group = models.ManyToManyField(Auth.Group, verbose_name=_('Denied Group'), related_name='denied_menus', blank=True)
	access_denied_user = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_('Denied User'), related_name='denied_menus', blank=True)

	access_denied_is_active = models.PositiveSmallIntegerField(verbose_name=_('Is active'), choices=BOOL_CHOICES, default=0)
	access_denied_is_staff = models.PositiveSmallIntegerField(verbose_name=_('Is staff'), choices=BOOL_CHOICES, default=0)
	access_denied_is_superuser = models.PositiveSmallIntegerField(verbose_name=_('Is superuser'), choices=BOOL_CHOICES, default=0)

	sites = models.ManyToManyField(Site, related_name='site_menu_items', verbose_name=_('Sites'), blank=True)

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
		try:
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
		except:
			return '#'

	def icon_preview(self):
		if self.icon:
			return '<img src="%s">' % self.icon.url
		else:
			return '(none)'
	icon_preview.short_description = _('Icon')
	icon_preview.allow_tags = True

	def order_puth(self, this):
		puth = str(this.sort) + ':' + str(this.id)
		if this.parent:
			return self.order_puth(this.parent) + '|' + puth
		else:
			return puth

	def get_level(self):
		if self.parent_id:
			return self.parent.get_level() + 1
		else:
			return 1

	def save(self, sort=True, *args, **kwargs):
		obj = super(Item, self).save(*args, **kwargs)
		self.childs_count = self.childs.count()
		self.url = self.get_absolute_url()
		self.level = self.get_level()
		self.order = self.order_puth(self)
		if self.parent:
			self.group = self.parent.group
		super(Item, self).save(*args, **kwargs)
		if sort:
			for item in self.childs.all():
				item.save()
		return obj

	def is_current(self, url):
		if self.url == url:
			return True
		else:
			return False

	def is_parent(self, url):
		childs = self.childs.filter(public=True)
		if childs:
			for item in childs:
				if item.url == url:
					return True
				else:
					return item.is_parent(url)
		else:
			return False

	def display(self):
		return '&nbsp;' * self.level * 8 + self.name
	display.short_description = _('Menu')
	display.allow_tags = True

	def __unicode__(self, *args, **kwargs):
		return self.name

	class Meta:
		ordering = ['order', 'sort']
		verbose_name = _('Menu')
		verbose_name_plural = _('Menus')


from django.db.models.signals import post_save
from django.dispatch import receiver
import logging


@receiver(post_save)
def update_links(sender, instance, **kwargs):
	if sender != Item:
		logging.warning('Update menu item')
		try:
			content_type = ContentType.objects.get_for_model(sender)
			for item in Item.objects.filter(content_type=content_type, object_id=instance.id):
				logging.warning('Save menu item %s' % item.id)
				item.save(sort=False)
		except:
			pass
