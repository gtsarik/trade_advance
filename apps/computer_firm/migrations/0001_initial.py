# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=50)),
                ('speed', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('hd', models.FloatField()),
                ('price', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2)),
                ('screen', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Laptop',
                'verbose_name_plural': 'Laptop',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=10)),
                ('speed', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('hd', models.FloatField()),
                ('cd', models.CharField(max_length=10)),
                ('price', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=1)),
                ('type_printer', models.CharField(max_length=50)),
                ('price', models.DecimalField(default=0, null=True, max_digits=12, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=50)),
                ('type_product', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('maker', models.ForeignKey(to='computer_firm.Maker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('context', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
