# Generated by Django 4.2.2 on 2023-09-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_message1_reciever_id_alter_message1_sender_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='adsgender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]
