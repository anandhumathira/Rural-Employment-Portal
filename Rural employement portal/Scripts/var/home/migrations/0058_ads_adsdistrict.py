# Generated by Django 4.2.6 on 2023-10-09 18:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0057_alter_newwork_empid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='adsdistrict',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
