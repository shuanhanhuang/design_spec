# Generated by Django 4.2.1 on 2023-10-06 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctable1', models.TextField(blank=True)),
                ('ctable2', models.TextField(blank=True)),
                ('cConform', models.CharField(max_length=10)),
                ('cPage', models.CharField(max_length=20)),
                ('cBrand', models.CharField(max_length=10)),
                ('cRemark', models.TextField(blank=True)),
                ('ref', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='details', to='specapp.spec')),
            ],
            options={
                'db_table': 'Compare',
            },
        ),
    ]