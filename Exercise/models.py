from django.db import models
from Users.models import Athlete
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class Domain(models.Model):
    title = models.CharField("Domain Name", max_length=50)
    set = models.PositiveSmallIntegerField("Set")
    count = models.PositiveIntegerField("Count")
    rest = models.PositiveSmallIntegerField("Rest Time")

    def __str__(self):
        return self.title

class ExerciseCategory(models.Model):
    title = models.CharField(verbose_name="Category Title", max_length=50)
    image = models.ImageField(
        "Category Image", upload_to='Exercise/Category/' , default='DE.png')
    parent = models.ForeignKey(
        "self", verbose_name='Parent',  on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    exercise_name = models.CharField("Exercise Name", max_length=50)
    exercise_details = models.TextField("Exercise Details")
    exercise_image = models.ImageField(
        "Exercise Image", upload_to='Exercise/', default='DE.png')
    exercise_category = models.ForeignKey(
        ExerciseCategory, verbose_name="Exercise Category", on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return self.exercise_name


class ExercisePlan(models.Model):
    STATUS = [
        ('CUT', 'cut'),
        ('UP', 'up'),
        ('DIET', 'diet'),
    ]

    start_date = models.DateField(verbose_name="Start Date", auto_now_add=True)
    end_date = models.DateField(verbose_name="End Date")
    status = models.CharField(verbose_name="Status",
                              choices=STATUS, max_length=50)
    athlete = models.ForeignKey(
        Athlete, verbose_name='Athlete', on_delete=models.CASCADE, null=True, blank=True)
    exercise = models.ManyToManyField(
        Exercise, verbose_name="Exercise", through="ExercisePlanItems")

    def __str__(self):
        return self.athlete.username


class ExercisePlanItems(models.Model):
    DAYS_OF_WEEK = [
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
    ]
    exercise_plan = models.ForeignKey(
        ExercisePlan, verbose_name="Exercise Plan", on_delete=models.CASCADE)
    exercise_category = models.ForeignKey(ExerciseCategory, verbose_name="Exercise Category", on_delete=models.CASCADE , null=True , blank=True)
    exercise = ChainedForeignKey(
        Exercise, verbose_name="Exercise", chained_field='exercise_category', chained_model_field = "exercise_category" , show_all=False , sort=True)
    domain = models.ForeignKey(Domain, verbose_name="Domain" , on_delete=models.CASCADE , null=True , blank=True)
    exercise_details = models.CharField(verbose_name="Exercise Details" , max_length=100)
    days = models.CharField(max_length=15, choices=DAYS_OF_WEEK , null=True , blank=True)

    def __str__(self):
        return f"{self.exercise.exercise_name} for {self.exercise_plan.athlete}"



