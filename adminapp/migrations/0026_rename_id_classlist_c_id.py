# Generated by Django 4.0.2 on 2022-04-06 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0025_rename_c_id_classlist_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classlist',
            old_name='id',
            new_name='c_id',
        ),
    ]