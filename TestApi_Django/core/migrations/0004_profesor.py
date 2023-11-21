# Generated by Django 4.1.5 on 2023-11-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alumno_rol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('idProfesor', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Usuario')),
                ('Gmail', models.CharField(max_length=50, verbose_name='Gmail')),
                ('Contrasena', models.CharField(max_length=50, verbose_name='Contrasena')),
                ('nombreProfesor', models.CharField(max_length=50, verbose_name='Nombre de Usuario')),
            ],
        ),
    ]