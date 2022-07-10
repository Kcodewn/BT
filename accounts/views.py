from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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

def ticket_details(request, pk):
    ticket_details = Ticket.objects.get(id=pk)
    context = {'ticket_details': ticket_details,}
    return render(request, 'accounts/ticket_details.html', context)

def create_projects(request):

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form': form}
    return render(request, 'accounts/create_projects.html', context)

def update_projects(request, pk):
    #ADD A delete_projects Please add a delete_project page please tahjnks 
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/create_projects.html', context)


def project_details(request, pk):
    project_details = Project.objects.get(id=pk)
    tickets = project_details.ticket_set.all()

    context = {'project_details': project_details, 'tickets': tickets}
    return render(request, 'accounts/project_details.html', context)

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