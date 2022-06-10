from django.contrib import admin

from .models import Domain, Exercise, ExerciseCategory, ExercisePlan, ExercisePlanItems

# Register your models here.
admin.site.register(Exercise)
admin.site.register(ExercisePlan)
admin.site.register(ExercisePlanItems)
admin.site.register(ExerciseCategory)
admin.site.register(Domain)