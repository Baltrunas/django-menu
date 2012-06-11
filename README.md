django-menu
=======

Simple tree menu for Django!

Added
=======
* MenuGroup public
* MenuGroup created_at
* MenuGroup updated_at
* Menu created_at
* Menu updated_at

Futures
=======
All
--------
* WYSIWYG ?
* Create new template ?
* Retranslate ?

Menu
--------
* order_puth
* save
* display
* __unicode__

Admin
--------
* WYSIWYG ?
* Form

How to use
=======
* add to INSTALLED_APPS
* syncdb
* collectstatic
{% load menu_tree %}
{% menu_tree main_menu 'menu_tree.html' request.path_info %}