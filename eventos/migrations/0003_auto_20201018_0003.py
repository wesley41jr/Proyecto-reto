# Generated by Django 2.2.16 on 2020-10-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20201017_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergeneral',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
