from django.urls import path 

from . import views 

app_name = 'tenants'

urlpatterns = [
    path('dashboard/', views.tenant_dashboard_view, name='dashboard'),
]