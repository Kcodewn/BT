from django.shortcuts import render
from django.http import HttpResponse
from .models import *

#SideBar Views 
def home(request):
    projects = Project.objects.all()
    tickets = Ticket.objects.all()
    new_tickets = tickets.filter(status='New Tickets').count()
    in_progress = tickets.filter(status='In Progress').count()
    urgent_tickets = tickets.filter(status='Urgent Tickets').count()
    resolved = tickets.filter(status='Resolved').count()


    context = {'projects': projects, 'tickets': tickets, 'new_tickets': new_tickets, 'in_progress': in_progress, 'urgent_tickets': urgent_tickets, 'resolved': resolved}

    return render(request, 'accounts/index.html', context)
    


def create_tickets(request):
    return render(request, 'accounts/create_tickets.html')

def my_tickets(request):
    return render(request, 'accounts/my_tickets.html')

def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'accounts/all_tickets.html', {'tickets': tickets})

def ticket_details(request):
 
#CURRENTLY TRYING TO GET DYNAMIC URL ROUTING!!!!!!!!!!!!!!!! 07/03 STILL WORKING ON DYNAMIC ROUTING 
    context = {'ticket_details': ticket_details,}
    return render(request, 'accounts/ticket_details.html', context)

def create_projects(request):
    return render(request, 'accounts/create_projects.html')

def project_details(request):
    return render(request, 'accounts/project_details.html')

def assign_users(request):
    return render(request, 'accounts/assign_users.html')

def remove_users(request):
    return render(request, 'accounts/remove_users.html')

def view_projects(request):
    projects = Project.objects.all()
    return render(request, 'accounts/view_projects.html', {'projects': projects})

def assign_roles(request):
    return render(request, 'accounts/assign_roles.html')

def remove_roles(request):
    return render(request, 'accounts/remove_roles.html')


#Pages Views


def charts(request):
    return render(request, 'accounts/charts.html')