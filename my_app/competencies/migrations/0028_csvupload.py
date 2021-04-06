# Generated by Django 3.1.4 on 2021-04-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competencies', '0027_auto_20210402_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='csvUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('csv_file', models.FileField(upload_to='csv')),
            ],
        ),
    ]