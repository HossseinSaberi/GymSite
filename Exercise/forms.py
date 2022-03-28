from django import forms
from .models import Domain, Exercise, ExerciseCategory, ExercisePlan, ExercisePlanItems

class CreateOrEditExercise(forms.ModelForm):
    class Meta:
        model  = Exercise
        fields = '__all__'
        widgets = {
            'exercise_image' : forms.FileInput(),
        }

    def __init__(self,*args, **kwargs):
        super(CreateOrEditExercise , self).__init__(*args, **kwargs)
        self.fields['exercise_image'].widget.attrs = {'id' : 'selectedFile'}


class CreateOrEditExercisePlan(forms.ModelForm):
    class Meta:
        model = ExercisePlan
        exclude = ['start_date' , 'exercise']

    
class CreateExercisePlanItem(forms.ModelForm):
    class Meta:
        model = ExercisePlanItems
        fields = '__all__'

    def __init__(self, exerciseplan ,  *args, **kwargs):
        super(CreateExercisePlanItem, self).__init__(*args, **kwargs)
        self.fields['exercise_plan'] = forms.ModelChoiceField(queryset= ExercisePlan.objects.filter(athlete__id=exerciseplan) , empty_label=None)

class EditExercisePlanItem(forms.ModelForm):
    class Meta:
        model = ExercisePlanItems
        exclude = ['exercise_plan',]


class CreateOrEditDomain(forms.ModelForm):
    class Meta:
        model = Domain
        fields = '__all__'



class CreateOrEditExerciseCategory(forms.ModelForm):
    class Meta:
        model = ExerciseCategory
        fields = '__all__'
        widgets = {
            'image' : forms.FileInput(),
        }

    def __init__(self,*args, **kwargs):
        super(CreateOrEditExerciseCategory , self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs = {'id' : 'selectedFile'}
