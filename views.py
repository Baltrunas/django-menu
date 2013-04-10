# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.core import urlresolvers
from django.template import RequestContext

from menu.models import Item

context = {}


def parent_tree(request, group_id=0, id=0):
	context['id'] = id
	context['menu'] = Item.objects.filter(group__id=group_id, parent=None).exclude(pk=id).order_by('sort')
	return render_to_response('menu/admin_tree.html', context, context_instance=RequestContext(request), mimetype='text/plain')


def url_patterns(request):
	resolver = urlresolvers.get_resolver(None)
	context['patterns'] = sorted([
			(key, value[0][0][0])
			for key, value in resolver.reverse_dict.items()
			if isinstance(key, basestring)
		])
	return render_to_response('menu/admin_url_patterns.html', context, context_instance=RequestContext(request), mimetype='text/plain')


def update(request):
	for item in Item.objects.all():
		item.save()
	return render_to_response('menu/update.html', context, context_instance=RequestContext(request), mimetype='text/plain')
