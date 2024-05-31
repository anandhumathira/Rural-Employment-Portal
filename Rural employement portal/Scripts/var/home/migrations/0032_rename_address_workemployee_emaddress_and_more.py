# Generated by Django 4.2.2 on 2023-08-10 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_rename_emaddress_workemployee_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workemployee',
            old_name='address',
            new_name='emaddress',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='adhar_no',
            new_name='emadhar',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='contact',
            new_name='emcontact',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='district',
            new_name='emdistrict',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='name',
            new_name='emname',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='panchayath',
            new_name='empanchayath',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='password',
            new_name='empassword',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='pincode',
            new_name='empincode',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='ratiocard_no',
            new_name='emratiocard',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='username',
            new_name='emusername',
        ),
        migrations.RenameField(
            model_name='workemployee',
            old_name='ward',
            new_name='emward',
        ),
    ]
