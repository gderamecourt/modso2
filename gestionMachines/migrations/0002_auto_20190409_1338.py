# Generated by Django 2.2 on 2019-04-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionMachines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modsouser',
            name='tel',
            field=models.CharField(max_length=10),
        ),
    ]
