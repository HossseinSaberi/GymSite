from django.contrib import admin
from .models import Medicine , MedicinePlan , MedicinePlanItems , MedicineCategory
# Register your models here.
admin.site.register(Medicine)
admin.site.register(MedicinePlan)
admin.site.register(MedicinePlanItems)
admin.site.register(MedicineCategory)