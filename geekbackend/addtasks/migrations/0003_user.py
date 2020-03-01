# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-18 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtasks', '0002_scan_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('privilege', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]