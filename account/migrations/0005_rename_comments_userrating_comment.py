# Generated by Django 4.2.7 on 2023-11-28 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userrating_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrating',
            old_name='comments',
            new_name='comment',
        ),
    ]