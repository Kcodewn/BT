from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from .filters import *

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
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form': form}
    return render(request, 'accounts/create_tickets.html', context)

def update_tickets(request, pk):
    update_tickets = Ticket.objects.get(id=pk)
    form = TicketForm(instance=update_tickets)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=update_tickets)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/create_tickets.html', context)

def delete_tickets(request,pk):
    delete_tickets = Ticket.objects.get(id=pk)
    if request.method == 'POST':
        delete_tickets.delete()
        return redirect('/')

    context = {'ticket': delete_tickets}
    return render(request, 'accounts/delete_tickets.html', context)



def my_tickets(request):
    
    return render(request, 'accounts/my_tickets.html')

def all_tickets(request):
    tickets = Ticket.objects.all()

    myFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = myFilter.qs

    context = {'tickets': tickets, 'myFilter': myFilter}
    return render(request, 'accounts/all_tickets.html', context)

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
    update_projects = Project.objects.get(id=pk)
    form = ProjectForm(instance=update_projects)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=update_projects)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/create_projects.html', context)

def delete_projects(request,pk):
    delete_projects = Project.objects.get(id=pk)
    if request.method == 'POST':
        delete_projects.delete()
        return redirect('/')

    context = {'project': delete_projects}
    return render(request, 'accounts/delete_projects.html', context)

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

    myFilter = ProjectFilter(request.GET, queryset=projects)
    projects = myFilter.qs

    context = {'projects': projects, 'myFilter': myFilter}
    return render(request, 'accounts/view_projects.html', context)

def assign_roles(request):
    return render(request, 'accounts/assign_roles.html')

def remove_roles(request):
    return render(request, 'accounts/remove_roles.html')


#Pages Views


def charts(request):
    return render(request, 'accounts/charts.html')