from django.db import models
from Users.models import  Athlete
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class FoodCategory(models.Model):
    title = models.CharField(verbose_name="Category Title", max_length=50)
    image = models.ImageField(
        "Category Image", upload_to='Food/Category/',  default='DF.jpg')
    parent = models.ForeignKey(
        "self", verbose_name='Parent',  on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Foods(models.Model):
    food_name = models.CharField(verbose_name="Food Name", max_length=50)
    food_image = models.ImageField(
        verbose_name="Food Image", upload_to='Food/',  default='DF.jpg')
    food_category = models.ForeignKey(
        FoodCategory, verbose_name="Food Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name


class FoodPlan(models.Model):
    STATUS = [
        ('CUT', 'cut'),
        ('UP', 'up'),
        ('DIET', 'diet'),
    ]

    start_date = models.DateField(verbose_name="Start Date", auto_now_add=True)
    end_date = models.DateField(verbose_name="End Date")
    status = models.CharField(verbose_name="Status",
                              choices=STATUS, max_length=50)
    # system_number = models.CharField(
    #     verbose_name="System Number", max_length=50)
    foods = models.ManyToManyField(
        Foods, through='FoodPlanItems',  verbose_name="Foods")
    athlete = models.ForeignKey(Athlete , verbose_name='Athlete' , on_delete=models.CASCADE , null=True , blank=True)




    def __str__(self) :
        return self.athlete.username


class FoodPlanItems(models.Model):
    DAYS_OF_WEEK = [
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
    ]
    food_plan = models.ForeignKey(
        FoodPlan, verbose_name="Food Plan", on_delete=models.CASCADE, related_name='foodplan_items')
    food_category = models.ForeignKey(FoodCategory, verbose_name="Food Category", on_delete=models.CASCADE , null=True , blank=True)
    foods =  ChainedForeignKey(
        Foods, verbose_name="Food", chained_field='food_category', chained_model_field = "food_category" , show_all=False , sort=True)
    food_details = models.CharField(verbose_name="Food Details" , max_length=100)

    count = models.PositiveIntegerField(verbose_name="Count")
    days = models.CharField(max_length=15, choices=DAYS_OF_WEEK)
    def __str__(self) :
        return f"{self.foods.food_name} for {self.food_plan.athlete}"
