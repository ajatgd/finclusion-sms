# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fincSMS', '0005_auto_20161107_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='aadhaaruid',
            new_name='aadhaar_uid',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='apy',
            new_name='atal_pension_yojana',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='lpg',
            new_name='lpg_subsidy',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='ny',
            new_name='new_services',
        ),
    ]
