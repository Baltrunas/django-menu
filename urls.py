from django.urls import path

from . import views

urlpatterns = [
	# Update
	path('update/', views.update, name='menu_update'),

	# URL to load url patterns for adding menu items
	path('url_patterns/', views.url_patterns, name='menu_url_patterns'),

	# Perens tree for menu item
	path('parent_tree/<int:group_id>/<int:id>/', views.parent_tree, name='menu_parent_tree'),

	# Perents tree url patterns template to replace in change form by ajax
	path('parent_tree/group_id/original_id/', views.parent_tree, name='menu_parent_tree_url_pattern'),
]
