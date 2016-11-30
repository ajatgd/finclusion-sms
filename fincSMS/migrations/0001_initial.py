# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(max_length=12)),
                ('salary', models.IntegerField(max_length=10)),
                ('category', models.CharField(choices=[('GENERAL', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], max_length=9)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('age', models.IntegerField(max_length=2)),
                ('aadhaaruid', models.IntegerField(max_length=2)),
                ('notifications', models.CharField(choices=[('LPG', 'LPG Schemes'), ('RATION', 'Ration Schemes'), ('APY', 'Atal Pension Yojana'), ('NY', 'New Yojanas')], max_length=20)),
            ],
        ),
    ]