# Generated by Django 4.1.7 on 2023-04-08 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_postdb_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdb',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
    ]