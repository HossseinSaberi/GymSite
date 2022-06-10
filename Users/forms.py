from django import forms
from .models import Athlete
class CreateOrEditAthlete(forms.ModelForm):
    class Meta:
        model = Athlete
        exclude = ['last_login' , 'date_joined' , 'groups' , 'user_permissions']
        widgets = {
            'user_image' : forms.FileInput(),
        }

    def __init__(self,*args, **kwargs):
        super(CreateOrEditAthlete , self).__init__(*args, **kwargs)
        self.fields['user_image'].widget.attrs = {'id' : 'selectedFile'}


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='UserName')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

