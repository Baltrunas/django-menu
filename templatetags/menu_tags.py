from django import template
register = template.Library()

from ..models import Item

from django.db.models import Q
from django.contrib.auth.models import User
user = User()


@register.simple_tag(takes_context=True)
def menu(context, group, parent=None, tpl_file='menu/default.html'):
	site = context['request'].site
	user = context['request'].user
	tpl = template.loader.get_template(tpl_file)
	tpl_context = {}
	tpl_context['request'] = context['request']
	if parent:
		tpl_context['level'] = parent.level + 1
	else:
		tpl_context['level'] = 1
	tpl_context['group'] = group
	tpl_context['parent'] = parent
	try:
		tpl_context['url'] = context['request'].META['PATH_INFO']
	except:
		tpl_context['url'] = ''


	menu = Item.objects.filter(public=True, parent=parent, group__slug=group, sites__in=[site]).order_by('sort')

	# ACCESS
	if user.is_authenticated:
		menu = menu.filter(
			Q(access='all') |
			Q(access='login_required') |
			Q(access='filter', access_user__in=[user]) |
			Q(access='filter', access_group__in=user.groups.all())
		).exclude(
			Q(access='anonymous_only') |
			Q(access='exclude', access_user__in=[user]) |
			Q(access='exclude', access_group__in=user.groups.all())
		).order_by('sort')
	else:
		menu = menu.filter(access__in=['all', 'anonymous_only'])

	tpl_context['menu'] = menu

	if tpl_context['menu']:
		return tpl.render(tpl_context)
	else:
		return ''


@register.filter
def is_current(instance, args):
	return instance.is_current(args)


@register.filter
def is_parent(instance, args):
	return instance.is_parent(args)


@register.simple_tag
def admin_menu_tree(parent, id):
	t = template.loader.get_template('menu/admin_tree.html')
	if hasattr(parent, 'childs'):
		childs = parent.childs.exclude(pk=id).order_by('sort')
		return t.render({'childs': childs, 'id': id})
	else:
		return t.render({'menu': parent, 'id': id})
