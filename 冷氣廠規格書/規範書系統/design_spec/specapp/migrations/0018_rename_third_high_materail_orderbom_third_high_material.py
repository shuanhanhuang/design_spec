# Generated by Django 4.2.1 on 2023-12-11 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0017_remove_orderbom_third_high_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderbom',
            old_name='third_high_materail',
            new_name='third_high_material',
        ),
    ]
