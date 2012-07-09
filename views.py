# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.template import RequestContext

from menu.models import *

from django.core import urlresolvers

def tree(request, group_id, id):
	context = {}
	context['id'] = id
	context['menu'] = Menu.objects.filter(group__id=group_id, parent=None).exclude(pk=id).order_by('sort')
	return render_to_response('admin/menu/menu/tree.html', context, context_instance=RequestContext(request), mimetype='text/plain')

def url_patterns(request):
	context = {}
	resolver = urlresolvers.get_resolver(None)
	context['patterns'] = sorted([
		(key, value[0][0][0])
		for key, value in resolver.reverse_dict.items()
		if isinstance(key, basestring)
	])
	return render_to_response('admin/menu/menu/url_patterns.html', context, context_instance=RequestContext(request), mimetype='text/plain')