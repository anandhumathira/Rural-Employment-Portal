# Generated by Django 4.2.2 on 2023-07-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_workrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=255)),
            ],
        ),
    ]
