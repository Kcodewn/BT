from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    #SideBar URLs#
    path('', views.home, name="home"),
    path('create_tickets/', views.create_tickets, name="create_tickets"),
    path('assign_roles/', views.assign_roles, name="assign_roles"),
    path('remove_roles/', views.remove_roles, name="remove_roles"),
    
    #Pages URLs
    path('charts/', views.charts, name="charts"),
]
