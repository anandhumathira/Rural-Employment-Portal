# Generated by Django 4.2.2 on 2023-09-18 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_alter_feedbacks_employeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newwork',
            name='empid',
            field=models.IntegerField(null=True),
        ),
    ]