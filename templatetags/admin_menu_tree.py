# -*- coding: utf-8 -*
from django import template
register = template.Library()


@register.simple_tag
def admin_menu_tree(parent, id):
	# level_space = '&nbsp;' * 8 * parent.level
	t = template.loader.get_template('menu/admin_tree.html')
	if hasattr(parent, 'childs'):
		childs = parent.childs.exclude(pk=id).order_by('sort')
		return t.render(template.Context({'childs': childs, 'id': id}))
	else:
		return t.render(template.Context({'menu': parent, 'id': id}))
