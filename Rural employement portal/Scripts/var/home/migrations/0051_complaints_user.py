# Generated by Django 4.2.2 on 2023-09-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_workrequest_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]