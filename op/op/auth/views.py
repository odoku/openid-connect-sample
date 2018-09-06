# -*- coding: utf-8 -*-

from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
)

from oidc_provider.models import Client


class LoginView(BaseLoginView):
    template_name = 'auth/login.html'


class LogoutView(BaseLogoutView):
    template_name = 'auth/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context
