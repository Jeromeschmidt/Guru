# Generated by Django 2.2.9 on 2020-02-24 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200218_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Bio',
            new_name='bio',
        ),
    ]
