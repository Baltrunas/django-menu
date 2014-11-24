# django-menu
Tree menu for Django

## Required
```'django.core.context_processors.request',```

## Install
* Add to INSTALLED_APPS ```'apps.menu',```
* Add to urls.py  ```url(r'^admin_tree_menu/', include('apps.menu.urls')),```
* manage.py syncdb
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
