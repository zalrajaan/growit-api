# Generated by Django 2.1.1 on 2018-09-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]