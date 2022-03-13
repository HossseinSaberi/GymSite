from django.urls import path
from .views import AthleteList ,DeleteAthlete , AthleteDetails , EditAthlete , MainPage , CreateAthlete , DeleteConfirm

urlpatterns = [
    path('', MainPage.as_view() , name = 'MainPage'),
    path('<int:athleteid>/DeleteConfirmAthlete/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:domainid>/DeleteConfirmDomain/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:exercisecategoryid>/DeleteConfirmExerciseCat/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:exerciseid>/DeleteConfirmExercise/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:exerciseplanid>/DeleteConfirmExercisePlan/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:exerciseplanitemid>/DeleteConfirmExercisePlanItem/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:foodid>/DeleteConfirmFood/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:foodplanid>/DeleteConfirmFoodPlan/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:foodplanitemid>/DeleteConfirmFoodPlanItem/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:foodcategoryid>/DeleteConfirmFoodCat/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:medicinecategoryid>/DeleteConfirmMedicineCat/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:medicineplanitemid>/DeleteConfirmMedicinePlanItem/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:medicineplanid>/DeleteConfirmMedicinePlan/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('<int:medicineid>/DeleteConfirmMedicine/', DeleteConfirm.as_view() , name = 'DeleteConfirm'),
    path('manage_athlete/' , AthleteList.as_view() , name='AthleteList'),
    path('manage_athlete/AddAthlete' , CreateAthlete.as_view() , name='AddAthlete'),
    path('manage_athlete/<int:pk>/DeleteAthlete/' , DeleteAthlete.as_view() , name='DeleteAthlete'),
    path('manage_athlete/<int:pk>/AthleteDetails/' , AthleteDetails.as_view() , name='AthleteDetails'),
    path('manage_athlete/<int:pk>/EditAthlete/' , EditAthlete.as_view() , name='EditAthlete'),
]