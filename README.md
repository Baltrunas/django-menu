django-menu
=======

Simple tree menu for Django!

Removed
=======
* WYSIWYG was removed to the essentials

Added
=======
* MenuGroup public
* MenuGroup created_at
* MenuGroup updated_at
* Menu created_at
* Menu updated_at

Fix
=======
* New translation for russian

Future fix
=======
* Create new template

* New form for admin
* order_puth
* save
* display
* __unicode__

* Add fixtures
* Add test

How to use
=======
* Add to INSTALLED_APPS
* manage.py syncdb
* manage.py collectstatic
{% load menu_tree %}
{% menu_tree main_menu 'menu_tree.html' request.path_info %}