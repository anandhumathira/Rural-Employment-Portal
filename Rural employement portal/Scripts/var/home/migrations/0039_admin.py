# Generated by Django 4.2.2 on 2023-09-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_workrequest_land_tax_receipt'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('usertype', models.CharField(default='admin', max_length=15)),
            ],
        ),
    ]