# Generated by Django 3.1 on 2022-09-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_email_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='messages_in_chat_page',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
