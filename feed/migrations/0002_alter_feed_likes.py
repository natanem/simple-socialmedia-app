# Generated by Django 4.0 on 2021-12-21 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feeds_liked', to='auth.user'),
        ),
    ]
