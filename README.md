# django-menu v4.0
Best tree menu for Django (1.4+)

# How to use
## Install
* Add to INSTALLED_APPS 'menu'
* Add to urls.py  url(r'^admin_tree_menu/', include('menu.urls')),
* Add to TEMPLATE_CONTEXT_PROCESSORS 'django.core.context_processors.request',
* manage.py syncdb
* manage.py collectstatic
	# RECOMENDATION to detect this URL
	# import
	from django.template import RequestContext
	# and view 
	return render_to_response('main.html', context, context_instance=RequestContext(request))

## Use
### In template:
{% load menu_tree %}
{% menu_tree 'main_menu' %}

# Futures
* Advanced Access Configuration
* Optimization
** menu_tree
** New translations
** Fixtures
** README.md
** Docs

# I think about
* Add FCBKcomplete for MenuGroup in admin interface.
* migrations
* https://github.com/jphalip/django-treemenus
<!-- 
	https://github.com/rossp/django-menu
	def save(self, force_insert=False, force_update=False):
		"""
		Re-order all items from 10 upwards, at intervals of 10.
		This makes it easy to insert new items in the middle of 
		existing items without having to manually shuffle 
		them all around.
		"""
		super(Menu, self).save(force_insert, force_update)
			
		current = 10
		for item in MenuItem.objects.filter(menu=self).order_by('order'):
			item.order = current
			item.save()
			current += 10
	 (Also see templatetags / menubuilder.py)
 -->

# Changelog
## 2012.10.22
### Add
* Translate to Deutsch
* Choise model type
* Options in template
* Start Advanced Access Configuration

# Changelog
## 2012.09.09
### Add
* Template filter to compare current url and menu item url
### Fix
* Ajax in the admin does not depend on the URL prefix
* Optimization urls.py

## 2012.09.08
### Add
* Access to model
* Level to model
### Fix
* Optimization admin

## 2012.09.07
### Add
* Add menu attributes for groups and items
### Fix
* Change tabs to spaces trying pep-8

## 2012.07.13
### Fix
* Bug with urls.py

## 2012.07.09
### Added
* include urls.py
* New views for admin

## 2012.07.08
### Added
* Add url type 'URLs' url from urls.py by name with paramentrs
* Optimized menu order_puth method.
* Optimized menu save method.
* Create new fixtures
* __MenuGroup complete!__ Maybe in the future MenuGroup will be changed but now I don `t know what could be improved.

## 2012.07.02
### Futures
* Modify the template tag so you do not need to use the view.
* Create new template


## 2012.07.01
### Added
* External and internal menu type
* New form for admin
* Fixtures

### Fix
* __unicode__
* Now use ugettext_lazy
* Same changes in display method
* Same changes in order_puth method

## 2012.06.17
### Added
* MenuGroup public
* MenuGroup created_at
* MenuGroup updated_at
* Menu created_at
* Menu updated_at

### Fix
* New translation for russian

### Removed
* WYSIWYG was removed to the essentials
