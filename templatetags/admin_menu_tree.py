# -*- coding: utf-8 -*
from django import template
register = template.Library()

@register.simple_tag
def admin_menu_tree(parent, id, level = 0):
	level += 1
	level_loop = [i for i in range(level)]
	t = template.loader.get_template('menu_menugroup_tree.html')
	if hasattr(parent, 'childs'):
		childs = parent.childs.exclude(pk=id).order_by('sort')
		return t.render(template.Context({'childs': childs, 'level': level, 'level_loop': level_loop, 'id': id}))
	else:
		return t.render(template.Context({'menu': parent, 'level': level, 'level_loop': level_loop, 'id': id}))