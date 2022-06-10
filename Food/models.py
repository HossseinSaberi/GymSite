from django.db import models
from Users.models import  Athlete
from smart_selects.db_fields import ChainedForeignKey
from jalali_date import date2jalali
from django_jalali.db import models as jmodels
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
        ('کات', 'کات'),
        ('افزایش وزن', 'افرایش وزن'),
        ('کاهش وزن', 'کاهش وزن'),
    ]

    start_date = jmodels.jDateField(verbose_name="Start Date", auto_now_add=True)
    end_date = jmodels.jDateField(verbose_name="End Date")
    status = models.CharField(verbose_name="Status",
                              choices=STATUS, max_length=50)
    # system_number = models.CharField(
    #     verbose_name="System Number", max_length=50)
    foods = models.ManyToManyField(
        Foods, through='FoodPlanItems',  verbose_name="Foods")
    athlete = models.ForeignKey(Athlete , verbose_name='Athlete' , on_delete=models.CASCADE , null=True , blank=True)




    def __str__(self) :
        return self.athlete.username

    def get_start_date(self):
            return date2jalali(self.start_date)

    def get_end_date(self):
        return date2jalali(self.end_date)

class FoodPlanItems(models.Model):
    DAYS_OF_WEEK = [
         ('شنبه', 'شنبه'),
        ('یکشنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه شنبه', 'سه شنبه'),
        ('چهارشنبه', 'چهارشنبه'),
        ('پنج شنبه', 'پنج شنبه'),
        ('جمعه', 'جمعه'),
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
