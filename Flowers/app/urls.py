from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('flowers/', views.all_flowers, name='all_flowers'),
    path('flowers/add/', views.add_flower, name='add_flower'),
    path('flowers/type/<int:type_id>/', views.flowers_by_type, name='flowers_by_type'),
    path('flowers/<int:flower_id>/', views.single_flower, name='single_flower'),
]