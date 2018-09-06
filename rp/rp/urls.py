# -*- coding: utf-8 -*-

import debug_toolbar
from django.contrib import admin
from django.contrib.auth.views import logout
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('openid/', include('mozilla_django_oidc.urls')),
    path('', include('rp.home.urls')),
    path('logout/', logout, name='logout'),
    path('__debug__/', include(debug_toolbar.urls)),
]
