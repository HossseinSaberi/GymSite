# Generated by Django 4.0.2 on 2022-02-10 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=50, verbose_name='Exercise Name')),
                ('exercise_details', models.TextField(max_length=50, verbose_name='Exercise Details')),
                ('exercise_image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Exercise Image')),
            ],
        ),
        migrations.CreateModel(
            name='ExercisePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('status', models.CharField(choices=[('CUT', 'cut'), ('UP', 'up'), ('DIET', 'diet')], max_length=50, verbose_name='Status')),
                ('athlete', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='ExercisePlanItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Count')),
                ('set', models.PositiveIntegerField(verbose_name='Set')),
                ('exercise_details', models.TextField(verbose_name='Exercise Details')),
                ('days', models.CharField(choices=[('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday'), ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday')], max_length=15)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercise.exercise', verbose_name='Exercise')),
                ('exercise_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercise.exerciseplan', verbose_name='Exercise Plan')),
            ],
        ),
        migrations.AddField(
            model_name='exerciseplan',
            name='exercise',
            field=models.ManyToManyField(through='Exercise.ExercisePlanItems', to='Exercise.Exercise', verbose_name='Exercise'),
        ),
        migrations.CreateModel(
            name='ExerciseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Category Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=None, verbose_name='Category Image')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Exercise.exercisecategory', verbose_name='Parent')),
            ],
        ),
    ]
