# Generated by Django 4.2.1 on 2024-03-31 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0036_spec_chaveorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='home',
        ),
        migrations.RemoveField(
            model_name='tablebom',
            name='SpecBOM',
        ),
        migrations.DeleteModel(
            name='OrderBOM',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
        migrations.DeleteModel(
            name='tableBOM',
        ),
    ]