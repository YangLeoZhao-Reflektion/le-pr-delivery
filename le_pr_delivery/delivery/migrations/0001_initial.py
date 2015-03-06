# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant_Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.TextField()),
                ('Link', models.TextField()),
                ('Yelp_Rating', models.IntegerField()),
                ('Category', models.TextField()),
                ('Last_Used', models.DateTimeField()),
                ('Total_Rating', models.IntegerField()),
                ('Total_Count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Email', models.EmailField(max_length=75)),
                ('Votes_Left', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Votes_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Votes', models.TextField()),
                ('Uid', models.ForeignKey(to='delivery.Users')),
                ('Vid', models.ForeignKey(to='delivery.Restaurants')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='restaurant_comments',
            name='Rid',
            field=models.ForeignKey(to='delivery.Restaurants'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant_comments',
            name='Uid',
            field=models.ForeignKey(to='delivery.Users'),
            preserve_default=True,
        ),
    ]
