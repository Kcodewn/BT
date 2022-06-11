from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('charts/', views.charts, name="charts"),
    path('assign_roles/', views.assign_roles, name="assign_roles"),

    
]
