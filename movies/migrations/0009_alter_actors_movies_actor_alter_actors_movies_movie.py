# Generated by Django 4.0.5 on 2022-07-06 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_actors_movies_actor_alter_actors_movies_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors_movies',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actormovies1', to='movies.actor'),
        ),
        migrations.AlterField(
            model_name='actors_movies',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actormovies2', to='movies.actor'),
        ),
    ]