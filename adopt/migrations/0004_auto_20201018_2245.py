# Generated by Django 3.1.2 on 2020-10-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0003_auto_20201018_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirreltest',
            name='above_ground',
            field=models.CharField(blank=True, default='', help_text='How Far from Ground Please Put The Number. If Found On The Ground Please Put FALSE', max_length=20),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('', '')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='color_note',
            field=models.CharField(blank=True, default='', help_text='Color Note', max_length=40),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='combi_fur',
            field=models.CharField(blank=True, default='', help_text='Combine Fur Color', max_length=40),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='highlight_fur',
            field=models.CharField(blank=True, default='', help_text='Highlight Fur Color', max_length=20),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='location',
            field=models.CharField(choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane'), ('', '')], default='', help_text='Locations', max_length=20),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='primary_fur',
            field=models.CharField(default='', help_text='Primary Fur Color', max_length=20),
        ),
        migrations.AddField(
            model_name='squirreltest',
            name='spec_loc',
            field=models.CharField(blank=True, default='', help_text='Specific Location', max_length=70),
        ),
    ]
