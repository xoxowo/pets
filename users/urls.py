from django.urls import URLPattern, path

from users.views import LoginView, SignUpView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
]