import json

from django.http import JsonResponse
from django.views import View

from movies.models import *

class ActorView(View):
# http -v get 127.0.0.1:8000/movies/actor
    def get(slef, request):
        #1.  배우 목록을 다 가져온다.
        actors = Actor.objects.all()
        results = []
        # for문을 사용하여 actors 모든 정보를 한개씩 빈 리스트에 넣어 출력 
        for actor in actors :
        #2 . 배우가 출연한 영화들을 가져온다. 여기에 MtoMfield 사용했다면 field 이름인actor.movies.all() 이렇게 가져오면됨 Movies.objects.filter(actor=actor)
            movies = actor.actormovies.all()
            movie_list=[]
        # 이중 for문을 사용하여 movies 모든 정보를 한개씩 moive_infor딕셔너리에 담고 다시 빈 리스트에 담는다  
            for a in movies:
                movie_info = {
                    "name" : a.movie.name,
                }
                movie_list.append(movie_info)
            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "date_of_birth" : actor.date_of_birth,
                    "movie" : movie_list,
                    }
            )       
        return JsonResponse({'resutls':results}, status=200)   
# http -v post 127.0.0.1:8000/movies/actor
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            date_of_birth = data['date_of_birth'],
        )
        return JsonResponse({'messasge':'created'}, status=201)   

class MoviesView(View):
# http -v get 127.0.0.1:8000/movies/movie 
    def get(slef, request):
        movies = Movie.objects.all()
        results = []
        # actors 모든 정보를 한개씩 넣어서 for문 사용
        for movie in movies :              
            actors = movie.actormovies.all() # mtom field를 사용했다면 역참조 actor.movies_set.all() 사용 가능.. ㄴ
            actor_list = []
            for i in actors :
                actor_info = {
                    "first_name":i.actor.first_name,
                    "last_name":i.actor.last_name,
                }
                actor_list.append(actor_info)

            results.append(
                {
                    "name" : movie.name,
                    "release_date" : movie.release_date,
                    "running_time" : movie.running_time,
                    "actor": actor_info,
                    }
            )       
        return JsonResponse({'resutls':results}, status=200)   
# http -v post 127.0.0.1:8000/movies/movie 
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            name = data['name'],
            release_date = data['release_date'],
            running_time = data['running_time'],
        )
        return JsonResponse({'messasge':'created'}, status=201)