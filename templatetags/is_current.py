# -*- utf-8 -*-
from django import template
register = template.Library()

@register.filter
def is_current(instance, args):
	return instance.is_current(args)
