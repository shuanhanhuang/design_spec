# Generated by Django 4.2.1 on 2023-12-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0008_alter_orderbom_eighteen_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='spec',
            name='cContact',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='spec',
            name='cContactTel',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='spec',
            name='cDate',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='spec',
            name='cDeliveryDate',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='spec',
            name='clocation',
            field=models.CharField(default='', max_length=50),
        ),
    ]
