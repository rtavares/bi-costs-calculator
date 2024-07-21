"""
URL configuration for products_prices project.

"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import (
    TemplateView,
)  # Initial project landing page. To be removed

urlpatterns = [
    # path('', TemplateView.as_view(template_name="startup.html"), name="home"),
    path("", include("products.urls", namespace="products")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
