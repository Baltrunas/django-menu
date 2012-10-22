# -*- utf-8 -*-
from django import template
register = template.Library()

@register.simple_tag
def attribute_list(list, place):
	t = template.loader.get_template('menu/attribute_list.html')
	return t.render(template.Context({'list': list, 'place': place}))
