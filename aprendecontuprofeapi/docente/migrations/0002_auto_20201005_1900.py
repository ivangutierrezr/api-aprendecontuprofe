# Generated by Django 3.1.1 on 2020-10-06 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='fechaNacimiento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='numeroCelular',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='numeroIdentificacion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='docente',
            name='numeroTelefonoFijo',
            field=models.CharField(max_length=50),
        ),
    ]