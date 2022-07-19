from django.urls import URLPattern, path
from movies.views import ActorView, MoviesView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', MoviesView.as_view()),
]