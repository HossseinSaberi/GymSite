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


class CreateMedicinePlanItem(forms.ModelForm):
    class Meta:
        model = MedicinePlanItems
        fields = '__all__'

    def __init__(self, medicineplan ,  *args, **kwargs):
        super(CreateMedicinePlanItem, self).__init__(*args, **kwargs)
        self.fields['medicine_plan'] = forms.ModelChoiceField(queryset= MedicinePlan.objects.filter(athlete__id=medicineplan) , empty_label=None)


class EditMedicinePlanItem(forms.ModelForm):
    class Meta:
        model = MedicinePlanItems
        exclude = ['medicine_plan' , ]
