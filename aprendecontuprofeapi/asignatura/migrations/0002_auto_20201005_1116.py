# Generated by Django 3.1.1 on 2020-10-05 16:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignatura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignatura',
            name='asistencias',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='evaluaciones',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='foro',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='respuestasEvaluaciones',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='respuestasTalleres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='asignatura',
            name='talleres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None),
        ),
    ]
