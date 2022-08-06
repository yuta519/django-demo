# Generated by Django 4.0.4 on 2022-07-17 02:49

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
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='ユーザ名')),
                ('age', models.IntegerField(default=20, verbose_name='年齢')),
                ('gender', models.CharField(max_length=5, verbose_name='性別')),
            ],
            options={
                'verbose_name': 'ユーザ',
                'verbose_name_plural': 'ユーザ',
                'db_table': 'users',
            },
        ),
    ]