# Generated by Django 2.2.16 on 2020-10-17 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.CharField(max_length=10)),
                ('boletos', models.CharField(max_length=5)),
                ('precio', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usergeneral',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('boletos', models.CharField(max_length=5)),
                ('telefono', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
            ],
        ),
    ]
