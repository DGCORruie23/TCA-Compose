# Generated by Django 4.2.6 on 2024-07-16 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0028_area_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='fecha_finalizacion',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
