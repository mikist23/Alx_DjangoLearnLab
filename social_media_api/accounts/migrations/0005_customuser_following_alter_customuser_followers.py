# Generated by Django 5.1.2 on 2024-12-17 13:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_post_author_delete_comment_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='user_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='user_followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
