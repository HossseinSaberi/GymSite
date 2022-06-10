from django import forms
from .models import Foods, FoodCategory, FoodPlan, FoodPlanItems


class CreateOrEditFood(forms.ModelForm):
    class Meta:
        model = Foods
        fields = '__all__'
        widgets = {
            'food_image': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateOrEditFood, self).__init__(*args, **kwargs)
        self.fields['food_image'].widget.attrs = {'id': 'selectedFile'}


class CreateOrEditFoodPlan(forms.ModelForm):
    class Meta:
        model = FoodPlan
        exclude = ['start_date', 'foods']


class CreateFoodPlanItem(forms.ModelForm):
    class Meta:
        model = FoodPlanItems
        fields = '__all__'

    def __init__(self, foodplan,  *args, **kwargs):
        super(CreateFoodPlanItem, self).__init__(*args, **kwargs)
        self.fields['food_plan'] = forms.ModelChoiceField(
            queryset=FoodPlan.objects.filter(athlete__id=foodplan), empty_label=None)


class EditFoodPlanItem(forms.ModelForm):
    class Meta:
        model = FoodPlanItems
        exclude = ['food_plan', ]


class CreateOrEditFoodCategory(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CreateOrEditFoodCategory, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs = {'id': 'selectedFile'}
