# Generated by Django 4.0.5 on 2022-07-05 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_actors_movies_actor_alter_actors_movies_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors_movies',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actormovies', to='movies.actor'),
        ),
        migrations.AlterField(
            model_name='actors_movies',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actormovies', to='movies.movie'),
        ),
    ]
