from django.db.models import fields
import django_filters
from .models import Exercise , ExerciseCategory , ExercisePlan , ExercisePlanItems


class ExercisePlanFilter(django_filters.FilterSet):
    # status = django_filters.CharFilter(field_name='status' , lookup_expr = 'eq')
    # athlete = django_filters.CharFilter(field_name='athlete' , lookup_expr = 'icontains')
    start_date = django_filters.CharFilter(field_name='start_date' , lookup_expr='gt')
    end_date = django_filters.CharFilter(field_name='end_date' , lookup_expr='lt')
    # athlete = django_filters.CharFilter(field_name='athlete__username' , lookup_expr='icontains')
    class Meta:
        model = ExercisePlan
        fields = ('status', 'start_date' , 'end_date' , 'athlete')
    


