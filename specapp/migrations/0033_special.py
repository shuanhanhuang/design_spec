# Generated by Django 4.2.1 on 2023-12-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0032_alter_orderbom_third_basic_medium_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cClient', models.CharField(default='', max_length=50)),
                ('cSpecial', models.TextField(blank=True)),
                ('cBrand', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'Special',
            },
        ),
    ]
