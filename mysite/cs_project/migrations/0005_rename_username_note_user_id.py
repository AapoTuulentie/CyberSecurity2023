# Generated by Django 4.1.7 on 2023-10-13 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_project', '0004_note_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='username',
            new_name='user_id',
        ),
    ]
