# Generated by Django 4.0.2 on 2022-03-13 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0008_alter_foodcategory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='image',
            field=models.ImageField(blank=True, default='static/DF.jpg', null=True, upload_to='Food/Category/', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='food_image',
            field=models.ImageField(blank=True, default='static/DF.jpg', null=True, upload_to='Food/', verbose_name='Food Image'),
        ),
    ]