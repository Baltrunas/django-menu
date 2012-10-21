# -*- coding: utf-8 -*
from menu.models import Item

from django.contrib.auth.models import User
user = User()

from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def menu_tree(context, group, tpl='menu/default.html', level=0):
	level += 1
	t = template.loader.get_template(tpl)
	if hasattr(group, 'childs'):
		try:
			url = context['url']
		except:
			url = ''

		user = context['request'].user
		if user.is_authenticated():
			from django.db.models import Q
			childs = Item.objects.filter(public=True, parent=group, access__in=[0, 2, 4, 5]).filter(
				Q(access=0) |
				Q(access=2) |
				Q(access=5, access_user__in=[user]) |
				Q(access=5, access_group__in=user.groups.all())
			).exclude(
				Q(access=4, access_user__in=[user]) |
				Q(access=4, access_group__in=user.groups.all())
			).order_by('sort')
		else:
			# Anonymous [All, Anonymous only]
			childs = Item.objects.filter(public=True, parent=group, access__in=[0, 1]).order_by('sort')

		return t.render(template.Context({'childs': childs, 'level': level, 'url': url, 'request': context['request']}))
	else:
		try:
			url = context['request'].META['PATH_INFO']
		except:
			url = ''
		# menu = Item.objects.filter(public=True, parent=None, group__slug=group).order_by('sort')
		if context['request'].user.is_authenticated():
			# All
			# Login required
			# access_user__in=id
			# access_user__in=id
			# Entry.objects.exclude(year=2006).filter(field='value')

			# from django.db.models import Q
			# Item.objects.filter(Q(creator=owner) | Q(moderated=False))

			menu = Item.objects.filter(public=True, parent=None, group__slug=group, access__in=[0, 2, 4, 5]).order_by('sort')
		else:
			# Anonymous [All, Anonymous only]
			menu = Item.objects.filter(public=True, parent=None, group__slug=group, access__in=[0, 1]).order_by('sort')
		return t.render(template.Context({'menu': menu, 'level': level, 'url': url, 'request': context['request']}))
