import django_tables2 as table
from Exercise.models import ExercisePlanItems

class ExercisePlanItemTable(table.Table):
    class Meta:
        model = ExercisePlanItems
        template_name = 'django_tables2/bootstrap4.html'