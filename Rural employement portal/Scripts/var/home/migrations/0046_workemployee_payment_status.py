# Generated by Django 4.2.2 on 2023-09-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_ads_adsemail_alter_panchayath_panchayath_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workemployee',
            name='payment_status',
            field=models.IntegerField(null=True),
        ),
    ]
