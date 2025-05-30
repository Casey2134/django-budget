# Generated by Django 5.2.1 on 2025-05-13 01:51

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='Updated')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='Is deleted')),
                ('transaction_type', models.CharField(choices=[('expense', 'Expense'), ('income', 'Income')], db_index=True, default='expense', max_length=32, verbose_name='Transaction type')),
                ('notes', models.CharField(blank=True, max_length=255, verbose_name='Notes')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Amount')),
                ('date', models.DateField(db_index=True, default=datetime.date.today, verbose_name='Date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
