# Generated by Django 3.1.4 on 2021-03-24 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competencies', '0005_auto_20210324_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='usertasktask',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competencies.task'),
        ),
    ]