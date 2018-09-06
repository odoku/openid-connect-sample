# -*- coding: utf-8 -*-

import debug_toolbar
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('', include('op.home.urls')),
    path('', include('op.auth.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
