# Generated by Django 4.1.6 on 2023-02-02 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
