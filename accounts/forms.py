from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
    
