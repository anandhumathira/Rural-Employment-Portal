# Generated by Django 4.2.2 on 2023-07-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_complaints_todate'),
    ]

    operations = [
        migrations.CreateModel(
            name='replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=255)),
                ('redate', models.DateField(null=True)),
            ],
        ),
    ]
