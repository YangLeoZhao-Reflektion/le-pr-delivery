# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comment', models.TextField()),
                ('Rid', models.ForeignKey(to='delivery.Restaurants')),
                ('Uid', models.ForeignKey(to='delivery.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VotesTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Votes', models.TextField()),
                ('Rid', models.ForeignKey(to='delivery.Restaurants')),
                ('Uid', models.ForeignKey(to='delivery.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='restaurant_comments',
            name='Rid',
        ),
        migrations.RemoveField(
            model_name='restaurant_comments',
            name='Uid',
        ),
        migrations.DeleteModel(
            name='Restaurant_Comments',
        ),
        migrations.RemoveField(
            model_name='votes_table',
            name='Uid',
        ),
        migrations.RemoveField(
            model_name='votes_table',
            name='Vid',
        ),
        migrations.DeleteModel(
            name='Votes_table',
        ),
    ]
