# Generated by Django 4.2.1 on 2023-12-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0029_orderbom_fourteen_budgetdollar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderbom',
            name='third_basic_frame',
            field=models.CharField(default='', max_length=30),
        ),
    ]