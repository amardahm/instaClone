# Generated by Django 2.2 on 2021-03-10 20:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210310_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, upload_to='post_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 23, 13, 925691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='like',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 23, 13, 925691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 23, 13, 925691, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
