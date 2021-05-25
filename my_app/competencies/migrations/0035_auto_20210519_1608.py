# Generated by Django 3.1.4 on 2021-05-19 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('competencies', '0034_auto_20210519_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertask',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='usertask',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]