# Generated by Django 4.2.2 on 2023-07-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_workcomplete'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('complaint', models.CharField(max_length=255)),
            ],
        ),
    ]