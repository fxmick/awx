# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

from django.conf.urls import url, include
from django.conf import settings
from awx.main.views import (
    handle_400,
    handle_403,
    handle_404,
    handle_500,
)


urlpatterns = [
    url(r'', include('awx.ui.urls', namespace='ui')),
    url(r'^api/', include('awx.api.urls', namespace='api')),
    url(r'^sso/', include('awx.sso.urls', namespace='sso')),
    url(r'^sso/', include('social_django.urls', namespace='social')),
    url(r'^(?:api/)?400.html$', handle_400),
    url(r'^(?:api/)?403.html$', handle_403),
    url(r'^(?:api/)?404.html$', handle_404),
    url(r'^(?:api/)?500.html$', handle_500),
]

if settings.SETTINGS_MODULE == 'awx.settings.development':
    try:
        import debug_toolbar
        urlpatterns += [
            # for Django version 2.0
            # path('__debug__/', include(debug_toolbar.urls)),

            # TODO: this is the Django < 2.0 version, REMOVEME
            url(r'^__debug__/', include(debug_toolbar.urls))
        ]
    except ImportError:
        pass

handler400 = 'awx.main.views.handle_400'
handler403 = 'awx.main.views.handle_403'
handler404 = 'awx.main.views.handle_404'
handler500 = 'awx.main.views.handle_500'
