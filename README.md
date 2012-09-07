# django-menu
Best tree menu for Django (1.4+)!

# Futures
* Optimization

# I think about
* Optimization model
* Optimization templates
* Help and docs
* Add FCBKcomplete for MenuGroup in admin interface.
* WYSIWYG to description

# How to use
## Install
* Add to INSTALLED_APPS 'menu'
* Add to urls.py  url(r'^menu/', include('menu.urls')),
* manage.py syncdb
* manage.py collectstatic

## Use
### In template:
{% load menu_tree %}
{% menu_tree 'main_menu' %}

# Changelog
## 2012.09.07
### Add
* Add menu options for groups and items

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
