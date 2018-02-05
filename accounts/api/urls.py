# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from accounts.api.views import view_all_categories, view_user_categories, view_single_category, register_category, \
    update_category, delete_category, view_all_accounts, view_user_accounts, view_single_account, register_account, \
    update_account, delete_account, view_all_movements, view_user_movements, view_single_movement, register_movement, \
    update_movement, delete_movement

urlpatterns = [
    # Categories
    url(r'^view_all_categories/$', view_all_categories, name='api_view_all_categories'),
    url(r'^view_user_categories/(?P<user_id>\d+)/$', view_user_categories, name='api_view_user_categories'),
    url(r'^view_single_category/(?P<category_id>\d+)/$', view_single_category, name='api_view_single_category'),
    url(r'^register_category/$', register_category, name='api_register_category'),
    url(r'^update_category/$', update_category, name='api_update_category'),
    url(r'^delete_category/$', delete_category, name='api_delete_category'),

    # Accounts
    url(r'^view_all_accounts/$', view_all_accounts, name='api_view_all_accounts'),
    url(r'^view_user_accounts/(?P<user_id>\d+)/$', view_user_accounts, name='api_view_user_accounts'),
    url(r'^view_single_account/(?P<account_id>\d+)/$', view_single_account, name='api_view_single_account'),
    url(r'^register_account/$', register_account, name='api_register_account'),
    url(r'^update_account/$', update_account, name='api_update_account'),
    url(r'^delete_account/$', delete_account, name='api_delete_account'),

    # Movement
    url(r'^view_all_movements/$', view_all_movements, name='api_view_all_movements'),
    url(r'^view_user_movements/(?P<user_id>\d+)/$', view_user_movements, name='api_view_user_movements'),
    url(r'^view_single_movement/(?P<movement_id>\d+)/$', view_single_movement, name='api_view_single_movement'),
    url(r'^register_movement/$', register_movement, name='api_register_movement'),
    url(r'^update_movement/$', update_movement, name='api_update_movement'),
    url(r'^delete_movement/$', delete_movement, name='api_delete_movement'),
]
