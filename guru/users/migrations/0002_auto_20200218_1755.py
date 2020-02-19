# Generated by Django 2.2.9 on 2020-02-18 17:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Bio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='avg_reponse',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='messages_received',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='support_classes_taken',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=20),
        ),
        migrations.AddField(
            model_name='user',
            name='support_skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=20),
        ),
    ]