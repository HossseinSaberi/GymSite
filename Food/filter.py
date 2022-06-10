from dataclasses import fields
import django_filters
from .models import FoodPlan


class FoodPlanFilter(django_filters.FilterSet):
    class Meta:
        model = FoodPlan
        fields  = ('status', 'start_date' , 'end_date' , 'athlete')