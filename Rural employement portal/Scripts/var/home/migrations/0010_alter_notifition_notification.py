# Generated by Django 4.2.2 on 2023-07-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_notifition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifition',
            name='notification',
            field=models.TextField(max_length=255),
        ),
    ]
