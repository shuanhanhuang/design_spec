# Generated by Django 4.2.1 on 2023-12-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0010_orderbom_televe_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbom',
            name='four_SSCR',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='four_material',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='four_way',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='seven_hotboard',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='seven_hotfins',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='seven_hotpipe_thick',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='seven_hotsize',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='seven_hotthick',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='seven_hotwaterpipe',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='six_axis',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='six_blade_material',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='six_form',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='orderbom',
            name='six_frame_material',
            field=models.CharField(default='', max_length=20),
        ),
    ]
