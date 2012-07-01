# django-menu
Best tree menu for Django!

# Futures
* Modify the template tag so you do not need to use the view.
* Create new template

# In plain
* New views and templates
* Optimization model, view, templates
* Optimization save method
* Add tests
* Add FCBKcomplete for MenuGroup in admin interface.

# How to use
## Install
* Add to INSTALLED_APPS 'menu'
* Add to urls.py  url(r'^admin/menu/group/(?P<group_id>\d)/(?P<id>\d)/$', 'menu.views.tree'),
* manage.py syncdb
* manage.py collectstatic

## Use
### In view:
main_menu = Menu.objects.filter(group__slug='main_menu', parent=None).order_by('sort')

### In template:
{% load menu_tree %}
{% menu_tree main_menu 'menu_tree.html' request.path_info %}


# Changelog
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
