# Generated by Django 3.2 on 2021-04-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutter3', '0003_alter_urlshort_user_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlshort',
            name='num_visits',
            field=models.IntegerField(default=0),
        ),
    ]
