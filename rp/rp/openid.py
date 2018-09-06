# -*- coding: utf-8 -*-

from django.conf import settings


def get_op_logout_url(request):
    return settings.OIDC_OP_LOGOUT_ENDPOINT
