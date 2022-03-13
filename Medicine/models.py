from django.db import models
from Users.models import Athlete
from smart_selects.db_fields import ChainedForeignKey
# Create your models here.
class MedicineCategory(models.Model):
    title = models.CharField(verbose_name="Category Title", max_length=50)
    image = models.ImageField(
        "Category Image", upload_to='Medicine/Category/', null=True, blank=True , default='static/DM.jpg')
    parent = models.ForeignKey(
        "self", verbose_name='Parent',  on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Medicine(models.Model):
    medicine_name = models.CharField(verbose_name="Medicine Name", max_length=50)
    medicine_image = models.ImageField(
        verbose_name="Medicine Image", upload_to='Medicine/', null=True, blank=True , default='static/DM.jpg')
    medicine_category = models.ForeignKey(
        MedicineCategory, verbose_name="Medicine Category", on_delete=models.CASCADE)


    
    def __str__(self) -> str:
        return self.medicine_name

class MedicinePlan(models.Model):
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
    medicine = models.ManyToManyField(
        Medicine, through='MedicinePlanItems',  verbose_name="Medicine")
    athlete = models.ForeignKey(Athlete , verbose_name='Athlete' , on_delete=models.CASCADE , null=True , blank=True)


    def __str__(self):
        return self.athlete.username

class MedicinePlanItems(models.Model):
    DAYS_OF_WEEK = [
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
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