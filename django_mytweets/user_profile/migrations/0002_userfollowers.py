# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField(default=1)),
                ('followers', models.ManyToManyField(related_name='followers', to='user_profile.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.User', unique=True)),
            ],
        ),
    ]
