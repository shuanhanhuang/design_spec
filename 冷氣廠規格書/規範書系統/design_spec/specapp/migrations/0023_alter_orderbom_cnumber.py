# Generated by Django 4.2.1 on 2023-12-12 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0022_alter_orderbom_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbom',
            name='cNumber',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9223372036854775807)]),
        ),
    ]
