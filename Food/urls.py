from django.urls import path
from .views import AddFood, FoodPlanList , FoodsList , EditFood , AddFoodPlan ,EditFoodPlan , CreateFoodPlanItems , EditFoodPlanItems , CreateFoodCategory , EditFoodCategory

urlpatterns = [
    path('' , FoodsList.as_view() , name='FoodList'),
    path('AddFood/' , AddFood.as_view() , name='AddFood'),
    path('<int:pk>/EditFood/' , EditFood.as_view() , name='EditFood'),
    path('FoodPlanList/' , FoodPlanList.as_view() , name='FoodPlanList'),
    path('AddFoodPlan/' , AddFoodPlan.as_view() , name='AddFoodPlan'),
    path('<int:pk>/EditFoodPlan/' , EditFoodPlan.as_view() , name='EditFoodPlan'),
    path('<int:pk>/FoodPlanItems/' , CreateFoodPlanItems.as_view() , name='CreateFoodPlanItems'),
    path('<int:id>/FoodPlanItems/<int:pk>/' , EditFoodPlanItems.as_view() , name='EditFoodPlanItems'),
    path('CreateFoodCategory/' , CreateFoodCategory.as_view() , name='CreateFoodCategory'),
    path('<int:pk>/EditFoodCategory/' , EditFoodCategory.as_view() , name='EditFoodCategory'),

]