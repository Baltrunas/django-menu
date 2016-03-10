# django-menu
Tree menu for Django

## Required
```'django.core.context_processors.request',```

## Install
* Add to INSTALLED_APPS ```'apps.menu',```
* Add to urls.py  ```url(r'^admin_tree_menu/', include('apps.menu.urls')),```
* manage.py migrate tree_menu
* manage.py collectstatic

## Use in template
```
{% load menu_tags %}
{% menu 'group', [parent=None], [tpl_file='menu/default.html'] %}
```

## TODO
* Optimization
* Take some ideas from https://github.com/jphalip/django-treemenus
* Documentation
* Advanced Access Configuration

☐ locale/
✔ static/
☐ templates/
	☐ admin
		☐ tree_menu
			☐ item
				☐ change_form.html
	☐ menu
		☐ admin_tree.html
		☐ admin_url_patterns.html
		☐ default.html
		☐ update.html
☐ templatetags/
	☐ __init__.py
	☐ menu_tags.py
☐ __init__.py
☐ admin.py
✔ apps.py
☐ models.py
✔ readme.md
☐ translation.py
☐ urls.py
☐ views.py