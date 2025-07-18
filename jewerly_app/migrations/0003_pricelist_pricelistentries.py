# Generated by Django 5.2.3 on 2025-07-11 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewerly_app', '0002_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'price_lists',
            },
        ),
        migrations.CreateModel(
            name='PriceListEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewerly_app.material')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewerly_app.pricelist')),
            ],
            options={
                'db_table': 'price_list_entries',
            },
        ),
    ]
