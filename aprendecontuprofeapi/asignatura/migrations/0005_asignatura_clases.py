# Generated by Django 3.1.1 on 2020-10-07 21:21

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignatura', '0004_auto_20201006_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='clases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None),
        ),
    ]
