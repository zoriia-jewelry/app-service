# Generated by Django 5.2.3 on 2025-07-11 18:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewerly_app', '0005_client_rename_pricelistentries_pricelistentry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialAuditEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewerly_app.client')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jewerly_app.material')),
            ],
        ),
    ]
