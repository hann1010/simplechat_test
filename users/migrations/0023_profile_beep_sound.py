# Generated by Django 3.2 on 2022-12-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_profile_initial_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='beep_sound',
            field=models.BooleanField(default=False),
        ),
    ]