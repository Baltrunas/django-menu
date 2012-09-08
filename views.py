# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.core import urlresolvers
from django.template import RequestContext

from menu.models import Item


def tree(request, group_id, id):
	context = {}
	context['id'] = id
	context['menu'] = Item.objects.filter(group__id=group_id, parent=None).exclude(pk=id).order_by('sort')
	return render_to_response('admin/menu/item/tree.html', context, context_instance=RequestContext(request), mimetype='text/plain')


def url_patterns(request):
	context = {}
	resolver = urlresolvers.get_resolver(None)
	context['patterns'] = sorted([
			(key, value[0][0][0])
			for key, value in resolver.reverse_dict.items()
			if isinstance(key, basestring)
		])
	return render_to_response('admin/menu/item/url_patterns.html', context, context_instance=RequestContext(request), mimetype='text/plain')
