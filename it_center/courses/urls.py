from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_lesson/', views.add_lesson, name='add_lesson'),
]