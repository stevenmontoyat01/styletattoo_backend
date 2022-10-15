# Generated by Django 3.2.9 on 2022-09-19 15:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fk_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tatoo.departamentos')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroUsuarios',
            fields=[
                ('id_user', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.TextField()),
                ('email', models.TextField(max_length=90)),
                ('fecha_nacimiento', models.DateField()),
                ('contraseña', models.TextField(max_length=20)),
                ('estado', models.CharField(default='A', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroTatuadores',
            fields=[
                ('id_tatuador', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.TextField()),
                ('genero', models.TextField()),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.TextField()),
                ('email', models.TextField(max_length=90)),
                ('experiencia', models.CharField(max_length=3)),
                ('descripcion', models.TextField(blank=True, default='', max_length=150)),
                ('contraseña', models.TextField(max_length=20)),
                ('estado', models.CharField(default='A', max_length=1)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tatoo.localidades')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tatoo.departamentos')),
            ],
        ),
        migrations.CreateModel(
            name='Portafolio_Tatuadores',
            fields=[
                ('id_publicacion', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha_publicacion', models.DateTimeField(default=datetime.datetime(2022, 9, 19, 10, 48, 23, 687892))),
                ('imagen', models.ImageField(upload_to='')),
                ('descripcion', models.TextField(blank=True, default='', max_length=150)),
                ('tatuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tatoo.registrotatuadores')),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id_likes', models.BigAutoField(primary_key=True, serialize=False)),
                ('likes', models.IntegerField()),
                ('fk_tatuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tatoo.registrotatuadores')),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id_cita', models.BigAutoField(primary_key=True, serialize=False)),
                ('Fecha', models.DateField()),
                ('Hora', models.TimeField()),
                ('Imagen', models.ImageField(upload_to='')),
                ('Descripcion', models.CharField(default='', max_length=150)),
                ('Tatuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tatoo.registrotatuadores')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tatoo.registrousuarios')),
            ],
        ),
    ]
