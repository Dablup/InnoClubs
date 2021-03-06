# Generated by Django 3.1.2 on 2020-11-08 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0007_auto_20201108_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.club'),
        ),
        migrations.AlterField(
            model_name='news',
            name='due_date',
            field=models.DateField(verbose_name='Due_date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publication_date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=32, verbose_name='Title'),
        ),
    ]
