# Generated by Django 4.1.7 on 2023-04-08 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_post_postdb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postdb',
            options={'ordering': ['profile', 'body', 'created', 'updated'], 'verbose_name': 'PostDB', 'verbose_name_plural': "user's Post"},
        ),
    ]