# Generated by Django 2.0.2 on 2018-02-15 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('title', models.TextField(blank=True)),
                ('detail', models.TextField(blank=True)),
                ('publish_date', models.DateTimeField(null=True)),
                ('body', models.TextField(blank=True)),
                ('url', models.CharField(blank=True, max_length=500)),
                ('label', models.CharField(blank=True, max_length=10)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'st_feeds',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='FeedRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=1, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editors', to=settings.AUTH_USER_MODEL)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_editors', to='st_api.Feed')),
            ],
            options={
                'db_table': 'st_feed_ratings',
                'ordering': ('created',),
            },
        ),
    ]
