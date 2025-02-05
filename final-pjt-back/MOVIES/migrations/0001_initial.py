

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(blank=True, max_length=60, null=True)),
                ('videos', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.CharField(blank=True, max_length=60, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('poster_path', models.CharField(blank=True, max_length=60, null=True)),
                ('popularity', models.FloatField()),
                ('overview', models.TextField(blank=True, null=True)),
                ('runtime', models.IntegerField(blank=True, null=True)),
                ('director', models.CharField(blank=True, max_length=50, null=True)),
                ('videos', models.TextField(blank=True, null=True)),
                ('actors', models.ManyToManyField(blank=True, to='MOVIES.actor')),
                ('dislike_movie_users', models.ManyToManyField(blank=True, related_name='dislike_movies', to=settings.AUTH_USER_MODEL)),
                ('favorite_movie_users', models.ManyToManyField(blank=True, related_name='favorite_movies', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(blank=True, to='MOVIES.genre')),
                ('like_movie_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('watching_movie_users', models.ManyToManyField(blank=True, related_name='watching_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
