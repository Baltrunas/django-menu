# -*- coding: utf-8 -*
from django import template
register = template.Library()

@register.simple_tag
def menu_tree(parent, tpl = 'menu_tree.html', url = '', level = 0):
	level += 1
	if level > 1:
		level_loop = [i for i in range(2, level)]
	else:
		level_loop = []
	t = template.loader.get_template(tpl)
	if hasattr(parent, 'childs'):
		childs = parent.childs.all().order_by('sort')
		return t.render(template.Context({'childs': childs, 'level': level, 'level_loop': level_loop, 'url': url}))
	else:
		return t.render(template.Context({'menu': parent, 'level': level, 'level_loop': level_loop, 'url': url}))