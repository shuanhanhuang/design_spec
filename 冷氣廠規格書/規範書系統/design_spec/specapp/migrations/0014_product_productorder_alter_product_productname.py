# Generated by Django 4.2.1 on 2023-12-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0013_remove_product_productcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productorder',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='productName',
            field=models.CharField(default='', max_length=150),
        ),
    ]
