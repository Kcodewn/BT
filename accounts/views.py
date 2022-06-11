from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/index.html')

def charts(request):
    return render(request, 'accounts/charts.html')
    

