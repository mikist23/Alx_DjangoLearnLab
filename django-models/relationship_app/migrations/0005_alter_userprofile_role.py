# Generated by Django 5.1.2 on 2024-11-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_book_options_book_published_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')], max_length=20),
        ),
    ]