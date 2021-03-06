# Generated by Django 4.0.2 on 2022-02-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0004_exercise_exercise_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Domain Name')),
                ('set', models.PositiveSmallIntegerField(verbose_name='Set')),
                ('count', models.PositiveIntegerField(verbose_name='Count')),
                ('rest', models.PositiveSmallIntegerField(verbose_name='Rest Time')),
            ],
        ),
        migrations.RemoveField(
            model_name='exerciseplanitems',
            name='count',
        ),
        migrations.RemoveField(
            model_name='exerciseplanitems',
            name='set',
        ),
        migrations.AlterField(
            model_name='exerciseplanitems',
            name='days',
            field=models.CharField(blank=True, choices=[('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday'), ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseplanitems',
            name='exercise_details',
            field=models.CharField(max_length=100, verbose_name='Exercise Details'),
        ),
    ]
