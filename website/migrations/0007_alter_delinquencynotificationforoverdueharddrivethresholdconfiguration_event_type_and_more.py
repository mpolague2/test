# Generated by Django 4.0.4 on 2022-04-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_delinquencynotificationforoverdueharddrivethresholdconfiguration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delinquencynotificationforoverdueharddrivethresholdconfiguration',
            name='event_type',
            field=models.CharField(choices=[], max_length=50),
        ),
        migrations.AlterField(
            model_name='forecastedrequestnotificationthresholdconfiguration',
            name='event_type',
            field=models.CharField(choices=[], max_length=50),
        ),
    ]
