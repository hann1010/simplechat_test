# Generated by Django 3.1 on 2022-08-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat_post',
            name='author_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
