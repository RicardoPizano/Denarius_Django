# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from users.api.views import view_users, register_user, delete_user, update_user

urlpatterns = [
    url(r'^view_all_users/', view_users, name='api_view_users'),

    url(r'^register_user/$', register_user, name='api_register_user'),
    url(r'^delete_user/$', delete_user, name='api_delete_user'),
    url(r'^update_user/$', update_user, name='api_update_user'),
]
