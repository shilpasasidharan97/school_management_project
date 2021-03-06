# Generated by Django 4.0.2 on 2022-03-24 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('classes', models.IntegerField()),
                ('division', models.CharField(max_length=2)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.teacherbasic')),
            ],
            options={
                'db_table': 'classes',
            },
        ),
    ]
