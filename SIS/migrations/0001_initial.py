# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-29 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('present', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='')),
                ('specialization', models.CharField(max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual_leave', models.IntegerField(default=7)),
                ('earned_leave', models.IntegerField(default=10)),
                ('sick_leave', models.IntegerField(default=8)),
                ('faculty', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='SIS.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('type', models.IntegerField(choices=[(1, 'Sick'), (2, 'Casual'), (3, 'Earned')], default=3)),
                ('status', models.IntegerField(choices=[(1, 'Accepted'), (2, 'Rejected'), (3, 'Pending')], default=3)),
                ('reason', models.CharField(max_length=900)),
                ('verdict', models.CharField(max_length=900, null=True)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='request', to='SIS.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='SelectedSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to='', verbose_name='Profile Image')),
                ('DOB', models.DateField()),
                ('reg', models.CharField(default=None, max_length=12, null=True)),
                ('tenth_marks', models.FloatField(default=0, verbose_name='HSC Marks')),
                ('inter_marks', models.FloatField(default=0, verbose_name='Current CGPA')),
                ('current_marks', models.FloatField(default=0, verbose_name='Overall CGPA')),
                ('branch', models.CharField(choices=[('Computer Science & Engineering', 'Computer Science & Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Others', 'Others')], default='Computer Science & Engineering', max_length=100)),
                ('year', models.IntegerField(choices=[(1, 'Ist Year'), (2, 'IInd Year'), (3, 'IIIrd Year'), (4, 'IVth Year')], default=1)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teaches', to='SIS.Faculty')),
            ],
        ),
        migrations.AddField(
            model_name='selectedsubject',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='selected', to='SIS.Student'),
        ),
        migrations.AddField(
            model_name='selectedsubject',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studies', to='SIS.Subject'),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='selected_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='SIS.SelectedSubject'),
        ),
    ]
