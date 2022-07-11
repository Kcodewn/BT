import django_filters
from django_filters import CharFilter
from .models import *

class ProjectFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['date_created', 'description']

class TicketFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['date_created', 'description']