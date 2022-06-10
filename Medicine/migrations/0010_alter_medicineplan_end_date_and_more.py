# Generated by Django 4.0.2 on 2022-06-05 10:16

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicine', '0009_alter_medicineplan_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineplan',
            name='end_date',
            field=django_jalali.db.models.jDateField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='medicineplan',
            name='start_date',
            field=django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='Start Date'),
        ),
    ]
