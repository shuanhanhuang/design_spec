# Generated by Django 4.2.1 on 2023-12-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0009_spec_ccontact_spec_ccontacttel_spec_cdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderbom',
            name='televe_material',
            field=models.CharField(default='', max_length=20),
        ),
    ]
