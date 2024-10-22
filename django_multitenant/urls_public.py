
from django.contrib import admin
from django.urls import path, include

from apps.tenants.admin import tenant_admin_site

urlpatterns = [

    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('admin_tenant/', tenant_admin_site.urls),
]
