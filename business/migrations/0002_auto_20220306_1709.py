# Generated by Django 3.2.7 on 2022-03-06 17:09

import business.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('date_joined', models.DateField(auto_created=True)),
                ('_id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('contact', models.CharField(max_length=255, unique=True)),
                ('picture', models.ImageField(upload_to=business.models.upload_to)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10),
        ),
    ]
