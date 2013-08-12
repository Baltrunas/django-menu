"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


# from menu.models import Item
# from django.contrib.sites.models import Site
# sites=Site.objects.all()
# x = 100 + 1
# for level_1 in range(1, x):
#     level_1_name = str(level_1)
#     level_1_item = Item(name=level_1_name, group_id=3, url_type='external')
#     level_1_item.save()
#     level_1_item.sites = sites
#     level_1_item.save()
#     for level_2 in xrange(1, x):
#         level_2_name = str(level_1) + '.' + str(level_2)
#         level_2_item = Item(name=level_2_name, group_id=3, parent=level_1_item, url_type='external')
#         level_2_item.save()
#         level_2_item.sites = sites
#         level_2_item.save()
#         for level_3 in xrange(1, x):
#             level_3_name = str(level_1) + '.' + str(level_2) + '.' + str(level_3)
#             level_3_item = Item(name=level_3_name, group_id=3, parent=level_2_item, url_type='external')
#             level_3_item.save()
#             level_3_item.sites = sites
#             level_3_item.save()

# class HelloTestCase(TestCase):
# 	fixtures = ['test_data.json']
