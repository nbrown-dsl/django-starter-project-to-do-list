# Generated by Django 3.1.4 on 2021-03-26 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competencies', '0019_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='competencies.requirement'),
        ),
    ]