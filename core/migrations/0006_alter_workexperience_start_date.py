# Generated by Django 3.2 on 2021-05-05 09:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_workexperience_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(datetime.date.today, 'Start date cannot exceed current date')]),
        ),
    ]
