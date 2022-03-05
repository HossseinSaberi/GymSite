from django.urls import path
from .views import CreateExercise, EditExercise , ExerciseList , DeleteExercise , ExercisePlanList , CreateExercisePlan , EditExercisePlan , CreateExercisePlanItems , EditExercisePlanItems , CreateDomain , CreateExerciseCategory , EditExerciseCategory , EditDomain


urlpatterns = [
    path('' , ExerciseList.as_view() , name='ExerciseList') , 
    path('CreateDomain/' , CreateDomain.as_view() , name='CreateDomain'),
    path('<int:pk>/EditDomain/' , EditDomain.as_view() , name='EditDomain'),
    path('CreateExerciseCategory/' , CreateExerciseCategory.as_view() , name='CreateExerciseCategory'),
    path('<int:pk>/EditExerciseCategory/' , EditExerciseCategory.as_view() , name='EditExerciseCategory'),
    path('CreateExercise/' , CreateExercise.as_view() , name='CreateExercise'),
    path('<int:pk>/EditExercise/', EditExercise.as_view() , name='EditExercise'),
    path('<int:pk>/DeleteExercise/', DeleteExercise.as_view() , name='DeleteExercise'),
    path('ExercisePlan/' , ExercisePlanList.as_view() , name='ExercisePlanList') , 
    path('CreateExercisePlan/' , CreateExercisePlan.as_view() , name='CreateExercisePlan'),
    path('<int:pk>/EditExercisePlan/' , EditExercisePlan.as_view() , name='EditExercisePlan'),
    path('<int:pk>/ExercisePlanItems/' , CreateExercisePlanItems.as_view() , name='CreateExercisePlanItems'),
    path('<int:id>/ExercisePlanItems/<int:pk>/' , EditExercisePlanItems.as_view() , name='EditExercisePlanItems'),
]
