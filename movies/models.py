from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    date_of_birth = models.IntegerField()
#   movies = models.manytomanyField('Moive', through= "Actors_movies") <- 실제 데이터 테이블이 생기는게 아니라 참조를 할 수 있는 그런 매니저가 생김
    
    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    name = models.CharField(max_length = 100)
    release_date = models.DateField(auto_now=False)
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'

class Actors_movies(models.Model):
    actor = models.ForeignKey('Actor', related_name='actormovies', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', related_name='actormovies', on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'


