# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('option', models.CharField(max_length=20)),
                ('auth_uname', models.CharField(max_length=200)),
                ('auth_pwd', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Index.Location'),
        ),
    ]
