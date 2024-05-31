# Generated by Django 4.2.2 on 2023-09-16 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_alter_pub_emailid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='adsemail',
            field=models.EmailField(error_messages={'unique': 'This email address is already in use.'}, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='panchayath',
            name='panchayath_email',
            field=models.EmailField(error_messages={'unique': 'This email address is already in use.'}, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='workemployee',
            name='emusername',
            field=models.CharField(error_messages={'unique': 'This email address is already in use.'}, max_length=150, unique=True),
        ),
    ]