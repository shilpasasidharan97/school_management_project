# Generated by Django 4.0.2 on 2022-04-06 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0023_remove_studentdetails_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherbasic',
            name='division',
        ),
        migrations.RemoveField(
            model_name='teacherbasic',
            name='handling_class',
        ),
        migrations.AddField(
            model_name='teacherbasic',
            name='classlist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='adminapp.classlist'),
        ),
    ]
