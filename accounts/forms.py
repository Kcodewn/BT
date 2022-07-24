from http.client import MULTIPLE_CHOICES
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
    

#why is this not workingggggggggggggggggggg 
#Havent worked on this in so long
class MemberForm(ModelForm):
    class Meta:
        model = Member 
        fields = '__all__'


class RoleForm(ModelForm):
    class Meta:
        model = Role 
        fields = '__all__'