import django_tables2 as table
from .models import Exercise

class ExerciseTable(table.Table):
    class Meta:
        model = Exercise
        # template_name = 'django_tables2/bootstrap4.html'
        # fields = '__all__'