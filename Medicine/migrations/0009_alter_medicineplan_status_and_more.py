# Generated by Django 4.0.2 on 2022-05-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicine', '0008_alter_medicineplanitems_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicineplan',
            name='status',
            field=models.CharField(choices=[('کات', 'کات'), ('افزایش وزن', 'افرایش وزن'), ('کاهش وزن', 'کاهش وزن')], max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='medicineplanitems',
            name='days',
            field=models.CharField(choices=[('شنبه', 'شنبه'), ('یکشنبه', 'یکشنبه'), ('دوشنبه', 'دوشنبه'), ('سه شنبه', 'سه شنبه'), ('چهارشنبه', 'چهارشنبه'), ('پنج شنبه', 'پنج شنبه'), ('جمعه', 'جمعه')], max_length=15),
        ),
    ]
