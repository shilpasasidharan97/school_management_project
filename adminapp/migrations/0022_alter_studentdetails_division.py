# Generated by Django 4.0.2 on 2022-04-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0021_studentdetails_classs_studentdetails_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='division',
            field=models.CharField(default='', max_length=5),
        ),
    ]