# Generated by Django 4.2.1 on 2023-11-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0007_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbom',
            name='eighteen_other',
            field=models.TextField(blank=True),
        ),
    ]
