# Generated by Django 4.2.1 on 2023-05-29 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='completed',
        ),
    ]
