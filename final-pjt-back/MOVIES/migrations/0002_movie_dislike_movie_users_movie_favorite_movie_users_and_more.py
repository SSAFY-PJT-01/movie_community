# Generated by Django 4.2.4 on 2023-11-19 11:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MOVIES', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='dislike_movie_users',
            field=models.ManyToManyField(blank=True, related_name='dislike_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='favorite_movie_users',
            field=models.ManyToManyField(blank=True, related_name='favorite_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='like_movie_users',
            field=models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='watching_movie_users',
            field=models.ManyToManyField(blank=True, related_name='watching_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
