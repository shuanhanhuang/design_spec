# Generated by Django 4.2.1 on 2023-11-26 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0004_spec_cbomfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cNumber', models.CharField(default='', max_length=50)),
                ('cContent', models.TextField(blank=True)),
                ('home', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='specapp.spec')),
            ],
            options={
                'db_table': 'OrderBOM',
            },
        ),
    ]