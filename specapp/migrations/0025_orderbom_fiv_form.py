# Generated by Django 4.2.1 on 2023-12-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0024_remove_product_productorder_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbom',
            name='fiv_form',
            field=models.CharField(default='', max_length=20),
        ),
    ]
