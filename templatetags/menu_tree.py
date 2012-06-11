# -*- coding: utf-8 -*
from django import template
register = template.Library()

@register.simple_tag
def menu_tree(parent, tpl = 'menu_tree.html', url = '', level = 0):
	level += 1
	t = template.loader.get_template(tpl)
	if hasattr(parent, 'childs'):
		childs = parent.childs.all()
		return t.render(template.Context({'childs': childs, 'level': level, 'url': url}))
	else:
		return t.render(template.Context({'menu': parent, 'level': level, 'url': url}))