# Generated by Django 2.2.8 on 2020-06-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teach',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
