# Generated by Django 3.2 on 2021-04-30 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_workexperience_currently_working_here'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
