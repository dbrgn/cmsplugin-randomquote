# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('quote_text', models.TextField(verbose_name='Quote Text')),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('author_url', models.URLField(default=None, null=True, blank=True, max_length=255, verbose_name='Author URL')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
