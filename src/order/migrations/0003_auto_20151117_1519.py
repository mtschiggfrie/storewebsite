# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20151117_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createorder',
            old_name='id',
            new_name='OrderId',
        ),
        migrations.AlterField(
            model_name='createorder',
            name='date',
            field=models.DateField(),
        ),
    ]
