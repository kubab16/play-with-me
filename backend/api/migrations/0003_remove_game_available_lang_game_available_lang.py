# Generated by Django 4.2 on 2023-05-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_genre_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='available_lang',
        ),
        migrations.AddField(
            model_name='game',
            name='available_lang',
            field=models.ManyToManyField(null=True, to='api.language'),
        ),
    ]