from django.shortcuts import render
from django.http import HttpResponse

#SideBar Views 
def home(request):
    return render(request, 'accounts/index.html')

def create_tickets(request):
    return render(request, 'accounts/create_tickets.html')
    
def assign_roles(request):
    return render(request, 'accounts/assign_roles.html')

def remove_roles(request):
    return render(request, 'accounts/remove_roles.html')


#Pages Views


def charts(request):
    return render(request, 'accounts/charts.html')