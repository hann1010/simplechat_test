# Generated by Django 3.1 on 2022-11-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat_post_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_post',
            name='author_nickname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]