# Generated by Django 2.1.4 on 2018-12-19 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_burd326_next_date_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='burd326',
            name='next_date_available',
            field=models.DateField(default=datetime.date(2018, 12, 19)),
        ),
    ]
