from django.contrib import admin
from django.urls import path, include

from storeapp import views

urlpatterns = [

    path('home',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('add/', views.person_create_view, name='person_add'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
    path('logout/', views.logout, name='logout'),

]