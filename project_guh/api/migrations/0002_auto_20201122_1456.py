# Generated by Django 3.1.3 on 2020-11-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earthquakes',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
