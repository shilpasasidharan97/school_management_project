# Generated by Django 4.0.2 on 2022-04-06 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0019_studentdetails_classes_classschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='classs',
        ),
        migrations.RemoveField(
            model_name='studentdetails',
            name='division',
        ),
    ]