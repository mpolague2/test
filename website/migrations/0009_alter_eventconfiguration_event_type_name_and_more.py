# Generated by Django 4.0.4 on 2022-04-17 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_delinquencynotificationforoverdueharddrivethresholdconfiguration_event_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventconfiguration',
            name='event_type_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='forecastedrequestnotificationthresholdconfiguration',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.eventconfiguration', to_field='event_type_name'),
        ),
    ]
