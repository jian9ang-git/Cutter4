# Generated by Django 3.2 on 2021-04-17 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutter3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshort',
            name='short_url',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='urlshort',
            name='user_url',
            field=models.CharField(max_length=2000),
        ),
    ]
