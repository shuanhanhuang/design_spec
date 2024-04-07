# Generated by Django 4.2.1 on 2023-12-10 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0011_orderbom_four_sscr_orderbom_four_material_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productCode', models.CharField(default='', max_length=50)),
                ('productName', models.CharField(default='', max_length=50)),
                ('productcount', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]