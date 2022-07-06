import json

from django.http import JsonResponse
from django.views import View

from pizza.models import *


class PizzaView(View):
    def post(self, request):
        data = json.loads(request.body)
        Pizza.objects.create(
            dough = data['dough'],
            size = data['size'],
        )
        return JsonResponse({'message':'created'}, status=201)
    def get(self,request):
        pizzas = Pizza.objects.all()
        results = []    
        for pizza in pizzas :
            topping = pizza.pizza_topping_set.all()
            topping_list=[]
            for i in topping :
                topping_info = {
                    "opsion1": i.topping.opsion1,
                    "opsion2": i.topping.opsion2,
                }
            topping_list.append(topping_info)
            results.append(
            {
                "dough" : pizza.dough,
                "size" : pizza.size,
                "opsion" :topping_list,
            } 
            )
        return JsonResponse({'resutls':results}, status=200)   


class ToppingView(View):
    def post(self, request):
        data = json.loads(request.body)
        Topping.objects.create(
            opsion1 = data['opsion1'],
            opsion2 = data['opsion2'],
        )
        return JsonResponse({'message':'created'}, status=201)        
    def get(self, request):
        toppings = Topping.objects.all()
        results=[]
        for topping in toppings :
            pizza = topping.pizza_topping_set.all()
            pizza_list = []
            for i in pizza :
                pizza_info ={
                    "dough": i.pizza.dough,
                    "size" : i.pizza.size,
                }
                pizza_list.append(pizza_info)
            results.append({
                "opsion1" : topping.opsion1,
                "opsion2" : topping.opsion2,
                "pizza_info" : pizza_list,
            }
            )
        return JsonResponse({'resutls':results}, status=200)   
        