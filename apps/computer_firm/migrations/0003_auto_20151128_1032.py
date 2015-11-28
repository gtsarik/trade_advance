# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computer_firm', '0002_tickets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='context',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
