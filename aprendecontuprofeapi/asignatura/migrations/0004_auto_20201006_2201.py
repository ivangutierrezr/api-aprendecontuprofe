# Generated by Django 3.1.1 on 2020-10-07 03:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignatura', '0003_auto_20201006_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='asistencias',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='estudiantes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='evaluaciones',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='foro',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='respuestasEvaluaciones',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='respuestasTalleres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='talleres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), blank=True, default=list, size=None),
        ),
    ]
