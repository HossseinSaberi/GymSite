from django.urls import path
from .views import AddMedicine, MedicinePlanList , MedicineList , EditMedicine , DeleteMedicine , AddMedicinePlan ,EditMedicinePlan , CreateMedicinePlanItems , EditMedicinePlanItems , CreateMedicineCategory , EditMedicineCategory

urlpatterns = [
    path('' , MedicineList.as_view() , name='MedicineList'),
    path('AddMedicine/' , AddMedicine.as_view() , name='AddMedicine'),
    path('<int:pk>/EditMedicine/' , EditMedicine.as_view() , name='EditMedicine'),
    path('<int:pk>/DeleteMedicine/' , DeleteMedicine.as_view() , name='DeleteMedicine'),
    path('MedicinePlanList/' , MedicinePlanList.as_view() , name='MedicinePlanList'),
    path('AddMedicinePlan/' , AddMedicinePlan.as_view() , name='AddMedicinePlan'),
    path('<int:pk>/EditMedicinePlan/' , EditMedicinePlan.as_view() , name='EditMedicinePlan'),
    path('<int:pk>/MedicinePlanItems/' , CreateMedicinePlanItems.as_view() , name='CreateMedicinePlanItems'),
    path('<int:id>/MedicinePlanItems/<int:pk>/' , EditMedicinePlanItems.as_view() , name='EditMedicinePlanItems'),
    path('CreateMedicineCategory/' , CreateMedicineCategory.as_view() , name='CreateMedicineCategory'),
    path('<int:pk>/EditMedicineCategory/' , EditMedicineCategory.as_view() , name='EditMedicineCategory'),

]