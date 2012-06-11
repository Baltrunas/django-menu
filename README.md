django-menu
=======

How to use
=======
* add to INSTALLED_APPS
* syncdb
* collectstatic
{% load menu_tree %}
{% menu_tree main_menu 'menu_tree.html' request.path_info %}



Simple tree menu for Django!