# Generated by Django 3.2.7 on 2021-09-09 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('can_get_username', 'Can get a username'), ('can_get_name', 'Can get a name'))},
        ),
    ]
