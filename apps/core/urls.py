from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.home, name='index'),
    path('add-item/', views.add_item, name='add-item'),
]