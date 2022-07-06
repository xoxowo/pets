from django.test import TestCase

from movies.models import Actor, Movie, Actors_movies
from movies.views import *
# Create your tests here.


for actor in Actor.objects.all() :
    print(actor.first_name)

