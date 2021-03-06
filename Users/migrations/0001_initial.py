# Generated by Django 4.0.2 on 2022-02-10 05:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('user_image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Profile Image')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('mobile_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator('^(?:0|98|\\+98|\\+980|0098|098|00980)?(9\\d{9})$')], verbose_name='Mobile Number')),
                ('is_mobile_submitted', models.BooleanField(default=False, verbose_name='is mobile submitted')),
                ('height', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Height')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='weight')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
