# Generated by Django 3.1 on 2022-10-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_profile_messages_in_chat_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
