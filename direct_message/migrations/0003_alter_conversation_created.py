# Generated by Django 4.0 on 2021-12-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct_message', '0002_message_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]