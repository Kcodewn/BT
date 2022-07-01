from django.shortcuts import render
from django.http import HttpResponse

#SideBar Views 
def home(request):
    return render(request, 'accounts/index.html')

def create_tickets(request):
    return render(request, 'accounts/create_tickets.html')

def my_tickets(request):
    return render(request, 'accounts/my_tickets.html')

def all_tickets(request):
    return render(request, 'accounts/all_tickets.html')

def create_projects(request):
    return render(request, 'accounts/create_projects.html')

def assign_users(request):
    return render(request, 'accounts/assign_users.html')

def remove_users(request):
    return render(request, 'accounts/remove_users.html')

def view_projects(request):
    return render(request, 'accounts/view_projects.html')

def assign_roles(request):
    return render(request, 'accounts/assign_roles.html')

def remove_roles(request):
    return render(request, 'accounts/remove_roles.html')


#Pages Views


def charts(request):
    return render(request, 'accounts/charts.html')