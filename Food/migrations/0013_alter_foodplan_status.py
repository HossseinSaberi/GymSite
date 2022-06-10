# Generated by Django 4.0.2 on 2022-05-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0012_alter_foodplanitems_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodplan',
            name='status',
            field=models.CharField(choices=[('کات', 'cut'), ('افزایش وزن', 'up'), ('کاهش وزن', 'diet')], max_length=50, verbose_name='Status'),
        ),
    ]
