# Generated by Django 4.1.5 on 2023-01-25 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landinghead',
            old_name='logo',
            new_name='logos',
        ),
    ]
