# Generated by Django 4.0.2 on 2022-02-25 08:37

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0007_exerciseplanitems_exercise_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseplanitems',
            name='exercise',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='exercise_category', chained_model_field='exercise_category', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='Exercise.exercise', verbose_name='Exercise'),
        ),
    ]