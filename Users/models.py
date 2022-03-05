from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.
PHONE_NUMBER_REGEX = RegexValidator(
    r'^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$')


class Athlete(AbstractUser): # if login lazem shod az abstrctuser ers bebar
    BODY_TYPE = [
        ('Ectomorphs', 'Ectomorphs'),
        ('Mesomorphs', 'Mesomorphs'),
        ('Endomorphs', 'Endomorphs'),
        ('Ecto-mesomorphs', 'Ecto-mesomorphs'),
        ('Meso-endomorphs', 'Meso-endomorphs'),
        ('Ecto-Endomorphs', 'Ecto-Endomorphs'),
    ]
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField('email address', unique=True)
    user_image = models.ImageField(
        'Profile Image',  upload_to=None, null=True, blank=True , default='static/nothing.jpg')
    address = models.TextField('Address',  null=True, blank=True)
    age = models.IntegerField('Age',  null=True, blank=True)
    mobile_number = models.CharField(
        'Mobile Number', max_length=15, unique=True,  validators=[PHONE_NUMBER_REGEX])
    is_mobile_submitted = models.BooleanField(
        'is mobile submitted', default=False)
    height = models.DecimalField('Height', max_digits=3, decimal_places=2 , null=True , blank=True)
    weight = models.DecimalField('weight', max_digits=3, decimal_places=1 , null=True , blank=True)
    body_type = models.CharField('Body Type', max_length=50 , choices=BODY_TYPE , null=True , blank=True)

    @property
    def bmi(self):
        user_bmi = self.weight / pow(self.height,2)
        return round(user_bmi , 1)

    @property
    def body_state(self):
        if self.bmi >= 31:
            return 'OBESE'
        elif self.bmi>=25 and self.bmi<31:
            return 'OVER WEIGHT'
        elif self.bmi>=18.5 and self.bmi<25:
            return 'NORMAL WEIGHT'
        if self.bmi >= 18.5:
            return 'UNDER WEIGHT'
        

    def __str__(self):
        return self.username

    
