from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    #SideBar URLs#
    path('', views.home, name="home"),
    path('create_tickets/', views.create_tickets, name="create_tickets"),
    path('all_tickets/', views.all_tickets, name="all_tickets"),
    path('my_tickets/', views.my_tickets, name="my_tickets"),
    path('ticket_details/<str:pk>/', views.ticket_details, name="ticket_details"),
    path('create_projects/', views.create_projects, name="create_projects"),
    path('update_projects/<str:pk>/', views.update_projects, name="update_projects"),
    path('project_details/<str:pk>/', views.project_details, name="project_details"),
    path('assign_users/', views.assign_users, name="assign_users"),
    path('remove_users/', views.remove_users, name="remove_users"),
    path('view_projects/', views.view_projects, name="view_projects"),
    path('assign_roles/', views.assign_roles, name="assign_roles"),
    path('remove_roles/', views.remove_roles, name="remove_roles"),
    
    #Pages URLs
    path('charts/', views.charts, name="charts"),
]
