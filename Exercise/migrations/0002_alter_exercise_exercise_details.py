# Generated by Django 4.0.2 on 2022-02-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_details',
            field=models.TextField(verbose_name='Exercise Details'),
        ),
    ]