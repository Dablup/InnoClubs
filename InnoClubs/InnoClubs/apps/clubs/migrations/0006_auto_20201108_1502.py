# Generated by Django 3.1.2 on 2020-11-08 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_auto_20201107_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubadmin',
            name='rights',
            field=models.CharField(max_length=9, verbose_name='Rights'),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
                ('info', models.TextField(verbose_name='Info')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication_date')),
                ('due_date', models.DateField(verbose_name='Due_date')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.club')),
            ],
        ),
    ]
