# Generated by Django 3.2 on 2021-04-17 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]
