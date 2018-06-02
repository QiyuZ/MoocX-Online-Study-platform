# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-26 22:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('desc', models.CharField(max_length=100, verbose_name='describe')),
                ('detail', models.TextField(verbose_name='detail')),
                ('degree', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=5)),
                ('duration', models.IntegerField(default=0, verbose_name='duration_mins')),
                ('student', models.IntegerField(default=0, verbose_name='students')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='fav_students')),
                ('image', models.ImageField(upload_to='course/%Y/%m', verbose_name='Pic')),
                ('clicks', models.IntegerField(default=0, verbose_name='clicks')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addTime')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='chapterName')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addTime')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='name')),
            ],
            options={
                'verbose_name': 'lesson',
                'verbose_name_plural': 'lesson',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='rescourceName')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addTime')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='resourceFile')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='name')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='videoName')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='addTime')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='chapter')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'video',
            },
        ),
    ]
