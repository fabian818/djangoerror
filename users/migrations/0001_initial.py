# Generated by Django 2.1 on 2018-08-18 18:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]