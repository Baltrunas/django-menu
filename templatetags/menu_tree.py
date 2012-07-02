# -*- coding: utf-8 -*
from django import template
register = template.Library()
from menu.models import Menu

@register.simple_tag(takes_context = True)
def menu_tree(context, group, tpl = 'menu_tree.html', level = 0):
	level += 1
	t = template.loader.get_template(tpl)
	if hasattr(group, 'childs'):
		url = context['url']
		childs = group.childs.filter(public=True).order_by('sort')
		return t.render(template.Context({'childs': childs, 'level': level, 'url': url}))
	else:
		url = context['request'].META['PATH_INFO']
		menu = Menu.objects.filter(public=True, parent=None, group__slug=group).order_by('sort')
		return t.render(template.Context({'menu': menu, 'level': level, 'url': url}))
