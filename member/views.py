import json

from django.http import JsonResponse
from django.views import View

from member.models import Owner, Pet

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name = data['name'],
            age = data['age'],
            email = data['email'],
        )
        return JsonResponse({'messasge':'created'}, status=201)    

    def get(self, request):
        owners = Owner.objects.all()
        results  = []
        for owner in owners:
            pets = owner.pet_set.all().values('name', 'age')

            results.append(
               {
                   "name" : owner.name,
                   "age" : owner.age,
                   "email" : owner.email,
                    "pet" : [pet for pet in pets ],
                }
           )       
        return JsonResponse({'resutls':results}, status=200)        

class PetView(View):
    def post(self, request):
        data = json.loads(request.body)
        Pet.objects.create(
            name = data['name'],
            age = data['age'],
            owner_id = data['owner_id'],
        )

        return JsonResponse({'messasge':'created'}, status=201)  

    def get(self, request):
        pets = Pet.objects.all()
        results = []

        for pet in pets :
            results.append(
                {
                    "name" : pet.name,
                    "age" : pet.age,
                    "owner": pet.owner.name
                }
            )
        return JsonResponse({'result':results}, status=200)