# Generated by Django 3.1.4 on 2021-01-20 17:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc

class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20210117_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 22, 17, 25, 14, 619905, tzinfo=utc)),
        ),
    ]
