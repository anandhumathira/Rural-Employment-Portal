# Generated by Django 4.2.6 on 2023-10-09 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_ads_adsdistrict'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrequest',
            name='district',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
