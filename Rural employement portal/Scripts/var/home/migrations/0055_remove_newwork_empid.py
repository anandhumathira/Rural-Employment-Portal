# Generated by Django 4.2.2 on 2023-09-18 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_alter_newwork_empid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newwork',
            name='empid',
        ),
    ]
