# Generated by Django 4.0.2 on 2022-04-06 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0017_alter_studentdetails_registration_num'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClassSchedule',
        ),
    ]
