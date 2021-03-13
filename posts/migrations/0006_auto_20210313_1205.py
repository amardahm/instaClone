# Generated by Django 2.2 on 2021-03-13 11:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_auto_20210310_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 3, 13, 11, 5, 53, 206805, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Post')),
            ],
        ),
        migrations.AlterField(
            model_name='like',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 11, 5, 53, 206805, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]