# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Braulio Zarate - Neurons Latam Inc
"""

from django.contrib import admin
from django.urls import path, include  # add this

from django.conf.urls.static import  static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
