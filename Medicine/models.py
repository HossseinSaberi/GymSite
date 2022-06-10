from django.db import models
from Users.models import Athlete
from smart_selects.db_fields import ChainedForeignKey
from jalali_date import date2jalali
from django_jalali.db import models as jmodels
# Create your models here.
class MedicineCategory(models.Model):
    title = models.CharField(verbose_name="Category Title", max_length=50)
    image = models.ImageField(
        "Category Image", upload_to='Medicine/Category/',  default='DM.jpg')
    parent = models.ForeignKey(
        "self", verbose_name='Parent',  on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Medicine(models.Model):
    medicine_name = models.CharField(verbose_name="Medicine Name", max_length=50)
    medicine_image = models.ImageField(
        verbose_name="Medicine Image", upload_to='Medicine/',  default='DM.jpg')
    medicine_category = models.ForeignKey(
        MedicineCategory, verbose_name="Medicine Category", on_delete=models.CASCADE)


    
    def __str__(self) -> str:
        return self.medicine_name

class MedicinePlan(models.Model):
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
    medicine = models.ManyToManyField(
        Medicine, through='MedicinePlanItems',  verbose_name="Medicine")
    athlete = models.ForeignKey(Athlete , verbose_name='Athlete' , on_delete=models.CASCADE , null=True , blank=True)


    def __str__(self):
        return self.athlete.username
    
    def get_start_date(self):
        return date2jalali(self.start_date)

    def get_end_date(self):
        return date2jalali(self.end_date)

class MedicinePlanItems(models.Model):
    DAYS_OF_WEEK = [
        ('شنبه', 'شنبه'),
        ('یکشنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه شنبه', 'سه شنبه'),
        ('چهارشنبه', 'چهارشنبه'),
        ('پنج شنبه', 'پنج شنبه'),
        ('جمعه', 'جمعه'),
    ]
    medicine_plan = models.ForeignKey(
        MedicinePlan, verbose_name="Medicine Plan", on_delete=models.CASCADE, related_name='medicineplan_items')
    medicine_category = models.ForeignKey(MedicineCategory, verbose_name="Food Category", on_delete=models.CASCADE , null=True , blank=True)
    medicine = ChainedForeignKey(
        Medicine, verbose_name="Medicine", chained_field="medicine_category" ,  chained_model_field = "medicine_category" , show_all=False , sort=True)
    count = models.PositiveIntegerField(verbose_name="Count")
    medicine_details = models.CharField(verbose_name="Medicine Details" , max_length=100)
    days = models.CharField(max_length=15, choices=DAYS_OF_WEEK)

    def __str__(self) :
        return f"{self.Medicine.medicine_name} for {self.medicine_plan.athlete}"