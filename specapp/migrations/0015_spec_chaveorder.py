# Generated by Django 4.2.1 on 2023-12-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0014_product_productorder_alter_product_productname'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='chaveorder',
            field=models.CharField(default='無', max_length=50),
        ),
    ]