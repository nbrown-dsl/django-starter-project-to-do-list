# Generated by Django 3.1.4 on 2021-04-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('competencies', '0029_auto_20210405_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='link',
            field=models.CharField(blank=True, default='dfdsf', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='role',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]