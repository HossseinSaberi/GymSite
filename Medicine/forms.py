from django import forms
from .models import Medicine, MedicineCategory, MedicinePlan, MedicinePlanItems 


class CreateOrEditMedicine (forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'medicine_image' : forms.FileInput(),
        }

    def __init__(self,*args, **kwargs):
        super(CreateOrEditMedicine , self).__init__(*args, **kwargs)
        self.fields['medicine_image'].widget.attrs = {'id' : 'selectedFile'}


class CreateOrEditMedicineCategory(forms.ModelForm):
    class Meta:
        model = MedicineCategory
        fields = '__all__'
        widgets = {
            'image' : forms.FileInput(),
        }

    def __init__(self,*args, **kwargs):
        super(CreateOrEditMedicineCategory , self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs = {'id' : 'selectedFile'}

        
class CreateOrEditMedicinePlan(forms.ModelForm):
    class Meta:
        model = MedicinePlan
        exclude = ['start_date' , 'medicine']


class CreateOrEditMedicinePlanItem(forms.ModelForm):
    class Meta:
        model = MedicinePlanItems
        fields = '__all__'