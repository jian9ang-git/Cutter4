# Generated by Django 3.2 on 2021-04-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutter3', '0005_urlshort_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshort',
            name='date',
            field=models.DateTimeField(default=None),
        ),
    ]
