# Generated by Django 3.1.4 on 2021-01-27 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_auto_20210127_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protocoltype',
            old_name='fields',
            new_name='protocolFields',
        ),
    ]
