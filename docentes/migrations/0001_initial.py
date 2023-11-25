# Generated by Django 4.2.7 on 2023-11-25 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('apellido', models.CharField(max_length=20)),
                ('cedula', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True)),
                ('email', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('numero', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('horas', models.IntegerField(null=True)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docentes.alumno')),
                ('institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docentes.institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('cedula', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, null=True)),
                ('email', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
                ('institucion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docentes.institucion')),
                ('materia', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docentes.materia')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='institucion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docentes.institucion'),
        ),
    ]
