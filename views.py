# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.template import RequestContext

from menu.models import *

def tree(request, group_id, id):
	context = {}
	context['menu'] = Menu.objects.filter(group__id=group_id, parent=None).exclude(pk=id).order_by('sort')
	context['id'] = id
	return render_to_response('menu_menugroup_tree.html', context, context_instance=RequestContext(request), mimetype='text/plain')