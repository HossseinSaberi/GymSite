import django_filters
from .models import MedicinePlan


class MedicinePlanFilter(django_filters.FilterSet):
    class Meta:
        model = MedicinePlan
        fields = ('status', 'start_date' , 'end_date' , 'athlete')