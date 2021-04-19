# Generated by Django 3.2 on 2021-04-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_url', models.URLField(max_length=2000)),
                ('short_url', models.URLField(default=None, max_length=2000)),
            ],
        ),
    ]