# -*- coding: utf-8 -*
from menu.models import Item

from django.db.models import Q
# from django.contrib.auth.models import User
# user = User()

from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def menu_tree(context, group, tpl='menu/default.html', level=0):
	level += 1
	t = template.loader.get_template(tpl)
	user = context['request'].user
	if hasattr(group, 'childs'):
		try:
			url = context['url']
		except:
			url = ''

		if user.is_authenticated():
			childs = Item.objects.filter(public=True, parent=group).filter(
				Q(access='all') |
				Q(access='login_required') |
				Q(access='filter', access_user__in=[user]) |
				Q(access='filter', access_group__in=user.groups.all())
			).exclude(
				Q(access='exclude', access_user__in=[user]) |
				Q(access='exclude', access_group__in=user.groups.all())
			).order_by('sort')
		else:
			# Anonymous [All, Anonymous only]
			childs = Item.objects.filter(public=True, parent=group, access__in=['all', 'anonymous_only']).order_by('sort')

		return t.render(template.Context({'childs': childs, 'level': level, 'url': url, 'request': context['request']}))
	else:
		try:
			url = context['request'].META['PATH_INFO']
		except:
			url = ''

		if user.is_authenticated():
			menu = Item.objects.filter(public=True, parent=None, group__slug=group).filter(
				Q(access='all') |
				Q(access='login_required') |
				Q(access='filter', access_user__in=[user]) |
				Q(access='filter', access_group__in=user.groups.all())
			).exclude(
				Q(access='exclude', access_user__in=[user]) |
				Q(access='exclude', access_group__in=user.groups.all())
			).order_by('sort')
		else:
			# Anonymous [All, Anonymous only]
			menu = Item.objects.filter(public=True, parent=None, group__slug=group, access__in=['all', 'anonymous_only']).order_by('sort')

		return t.render(template.Context({'menu': menu, 'level': level, 'url': url, 'request': context['request']}))
