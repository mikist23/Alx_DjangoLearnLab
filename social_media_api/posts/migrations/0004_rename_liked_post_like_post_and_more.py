# Generated by Django 5.1.2 on 2024-12-18 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='liked_post',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_like',
            new_name='user',
        ),
    ]