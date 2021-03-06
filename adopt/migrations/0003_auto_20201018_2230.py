# Generated by Django 3.1.2 on 2020-10-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0002_squirreltest'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirreltest',
            name='date',
            field=models.CharField(default='', max_length=9),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='hectare',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='hectare_sq',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=3),
        ),
        migrations.AlterField(
            model_name='squirreltest',
            name='unique_squirrel_id',
            field=models.CharField(default='', max_length=14),
        ),
        migrations.AlterField(
            model_name='squirreltest',
            name='x',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='squirreltest',
            name='y',
            field=models.FloatField(default=0),
        ),
    ]
