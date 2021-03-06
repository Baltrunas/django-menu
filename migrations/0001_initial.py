# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slug', models.SlugField(help_text='A slug is the part of a URL which identifies a page using human-readable keywords', max_length=128, verbose_name='Slug')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('sites', models.ManyToManyField(blank=True, related_name='menus', to='sites.Site', verbose_name='Sites')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Menu Group',
                'verbose_name_plural': 'Menu Groups',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('url_type', models.CharField(choices=[('internal', ((b'model-oblect', 'model oblect'), (b'url-patterns', 'url patterns'))), ('external', ((b'external', 'external'),))], max_length=20, verbose_name='URL Type')),
                ('url', models.CharField(blank=True, default=b'#', max_length=255, verbose_name='URL')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Object ID')),
                ('url_patterns', models.CharField(blank=True, max_length=255, verbose_name='url patterns')),
                ('url_options', models.TextField(blank=True, help_text=b'key1=value1<br>key2=value2', verbose_name='URL Options')),
                ('level', models.PositiveSmallIntegerField(blank=True, default=0, editable=False, null=True, verbose_name='Level')),
                ('childs_count', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='Childs Count')),
                ('left_key', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='Left Key')),
                ('right_key', models.PositiveIntegerField(blank=True, editable=False, null=True, verbose_name='Right Key')),
                ('order', models.SlugField(editable=False, max_length=255, verbose_name='Order')),
                ('sort', models.PositiveSmallIntegerField(default=500, verbose_name='Sort')),
                ('icon', models.ImageField(blank=True, upload_to=b'img/menu', verbose_name='Icon')),
                ('access', models.CharField(choices=[(b'all', 'All'), (b'anonymous_only', 'Anonymous only'), (b'login_required', 'Login required'), (b'exclude', 'Except'), (b'filter', 'Only'), (b'advanced_access', 'Advanced Access')], default=b'all', max_length=32, verbose_name='Access')),
                ('access_is_active', models.PositiveSmallIntegerField(choices=[(0, 'All'), (1, 'Yes'), (2, 'No')], default=0, verbose_name='Is active')),
                ('access_is_staff', models.PositiveSmallIntegerField(choices=[(0, 'All'), (1, 'Yes'), (2, 'No')], default=0, verbose_name='Is staff')),
                ('access_is_superuser', models.PositiveSmallIntegerField(choices=[(0, 'All'), (1, 'Yes'), (2, 'No')], default=0, verbose_name='Is superuser')),
                ('access_denied_is_active', models.PositiveSmallIntegerField(choices=[(0, 'All'), (1, 'Yes'), (2, 'No')], default=0, verbose_name='Is active')),
                ('access_denied_is_staff', models.PositiveSmallIntegerField(choices=[(0, 'All'), (1, 'Yes'), (2, 'No')], default=0, verbose_name='Is staff')),
                ('access_denied_is_superuser', models.PositiveSmallIntegerField(choices=[(0, 'All'), (1, 'Yes'), (2, 'No')], default=0, verbose_name='Is superuser')),
                ('public', models.BooleanField(default=True, verbose_name='Public')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('access_denied_group', models.ManyToManyField(blank=True, related_name='denied_menus', to='auth.Group', verbose_name='Denied Group')),
                ('access_denied_user', models.ManyToManyField(blank=True, related_name='denied_menus', to=settings.AUTH_USER_MODEL, verbose_name='Denied User')),
                ('access_group', models.ManyToManyField(blank=True, related_name='menus', to='auth.Group', verbose_name='Access Group')),
                ('access_user', models.ManyToManyField(blank=True, related_name='menus', to=settings.AUTH_USER_MODEL, verbose_name='Access User')),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Content Type')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='tree_menu.Group', verbose_name='Menu Group')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='tree_menu.Item', verbose_name='Parent')),
                ('sites', models.ManyToManyField(blank=True, related_name='site_menu_items', to='sites.Site', verbose_name='Sites')),
            ],
            options={
                'ordering': ['order', 'sort'],
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
