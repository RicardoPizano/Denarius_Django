# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

urlpatterns = [
    url(r'^accounts/', include('accounts.api.urls')),
    url(r'^users/', include('users.api.urls')),
]
