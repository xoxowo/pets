from django.urls import URLPattern, path
from pizza.views import *


urlpatterns = [
    path('/dough', PizzaView.as_view()),
    path('/topping', ToppingView.as_view()),
]