# Generated by Django 2.0.1 on 2018-02-27 19:11

from django.db import migrations
import server.models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', server.models.UserManager()),
            ],
        ),
    ]
