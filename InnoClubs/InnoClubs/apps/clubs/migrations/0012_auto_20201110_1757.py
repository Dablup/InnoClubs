# Generated by Django 3.1.2 on 2020-11-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0011_auto_20201110_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.ImageField(null=True, upload_to='static/img/events'),
        ),
        migrations.AddField(
            model_name='onetimeevent',
            name='img',
            field=models.ImageField(null=True, upload_to='static/img/events'),
        ),
        migrations.AlterField(
            model_name='onetimeevent',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
