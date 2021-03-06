# Generated by Django 3.1.7 on 2021-03-10 23:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210310_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
