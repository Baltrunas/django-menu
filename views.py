from django.shortcuts import render
# from django.core import urlresolvers
from django.urls.resolvers import get_resolver

from .models import Item


def parent_tree(request, group_id=0, id=0):
	context = {}
	context['id'] = id
	context['menu'] = Item.objects.filter(group__id=group_id, parent=None).exclude(pk=id).order_by('sort')
	return render(request, 'menu/admin_tree.html', context, content_type='text/plain')


def url_patterns(request):
	context = {}
	resolver = get_resolver(None)

	context['patterns'] = []
	for key, value in resolver.reverse_dict.items():
		if isinstance(key, str):
			url = {
				'url_name': key,
				'url_reg_ex': value[1],
				'url_param': value[0][0][1],
			}
			context['patterns'].append(url)

	return render(request, 'menu/admin_url_patterns.html', context, content_type='text/plain')


def update(request):
	context = {}
	for item in Item.objects.all():
		item.save()
	return render(request, 'menu/update.html', context, content_type='text/plain')
