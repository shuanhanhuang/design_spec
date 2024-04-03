# Generated by Django 4.2.1 on 2023-11-27 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specapp', '0006_remove_orderbom_ccontent_orderbom_eight_material_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cOrder', models.CharField(default='', max_length=50)),
                ('cCase', models.CharField(default='', max_length=50)),
                ('cCaseOp', models.CharField(default='', max_length=50)),
                ('cDelivery', models.CharField(default='', max_length=50)),
                ('cContact', models.CharField(default='', max_length=50)),
                ('cAddress', models.CharField(default='', max_length=50)),
                ('cOther', models.CharField(default='', max_length=50)),
                ('cMove', models.CharField(default='', max_length=50)),
                ('cMovecheck', models.CharField(default='', max_length=50)),
                ('cMoveBudget', models.CharField(default='', max_length=50)),
                ('cOnsite', models.CharField(default='', max_length=50)),
                ('cdaynight', models.CharField(default='', max_length=50)),
                ('cHour', models.CharField(default='', max_length=50)),
                ('cAssembleBudget', models.CharField(default='', max_length=50)),
                ('cInto', models.CharField(default='', max_length=50)),
                ('cAfterass', models.CharField(default='', max_length=50)),
                ('cForeigninto', models.CharField(default='', max_length=50)),
                ('cCard', models.CharField(default='', max_length=50)),
                ('cInsurance', models.CharField(default='', max_length=50)),
                ('cprepare', models.CharField(default='', max_length=50)),
                ('cProcurementad', models.CharField(default='', max_length=50)),
                ('cTest', models.CharField(default='', max_length=50)),
                ('cMoring', models.CharField(default='', max_length=50)),
                ('cERP', models.CharField(default='', max_length=50)),
                ('cLee', models.CharField(default='', max_length=50)),
                ('cBlower', models.CharField(default='', max_length=50)),
                ('cInternalother', models.CharField(default='', max_length=50)),
                ('cBoxing', models.CharField(default='', max_length=50)),
                ('cBoxingbudget', models.CharField(default='', max_length=50)),
                ('home', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='specapp.spec')),
            ],
            options={
                'db_table': 'Shipping',
            },
        ),
    ]
