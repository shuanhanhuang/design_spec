# Generated by Django 4.2.1 on 2023-12-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0020_alter_tablebom_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spec',
            name='chaveorder',
        ),
        migrations.AddField(
            model_name='tablebom',
            name='chaveorder',
            field=models.CharField(default='無', max_length=50),
        ),
        migrations.AlterField(
            model_name='orderbom',
            name='cNumber',
            field=models.IntegerField(default='', max_length=50),
        ),
    ]
