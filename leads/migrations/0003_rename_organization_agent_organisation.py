# Generated by Django 3.2.8 on 2021-11-06 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20211106_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='organization',
            new_name='organisation',
        ),
    ]