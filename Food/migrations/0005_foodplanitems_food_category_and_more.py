# Generated by Django 4.0.2 on 2022-03-01 09:42

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0004_alter_foodcategory_image_alter_foods_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodplanitems',
            name='food_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Food.foodcategory', verbose_name='Food Category'),
        ),
        migrations.AlterField(
            model_name='foodplanitems',
            name='foods',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='food_category', chained_model_field='food_category', on_delete=django.db.models.deletion.CASCADE, to='Food.foods', verbose_name='Exercise'),
        ),
    ]
