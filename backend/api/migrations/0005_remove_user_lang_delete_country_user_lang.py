# Generated by Django 4.2 on 2023-05-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lang',
        ),
        migrations.DeleteModel(
            name='COUNTRY',
        ),
        migrations.AddField(
            model_name='user',
            name='lang',
            field=models.ManyToManyField(to='api.language'),
        ),
    ]