# Generated by Django 3.1.4 on 2021-03-24 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competencies', '0007_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='userGrade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='competencies.grade'),
        ),
    ]