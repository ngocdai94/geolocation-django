# Generated by Django 3.0.5 on 2020-05-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocationapp', '0003_auto_20200528_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocationdata',
            name='latdirection',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='geolocationdata',
            name='longdirection',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
