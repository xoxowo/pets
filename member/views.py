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
        # owner의 모든 정보를 변수에 넣기
        owners = Owner.objects.all()
        # 빈 리스트 만들어서 for 문으로 owner 정보를 한개씩 넣어주기 append.({딕셔너리 방식으로!})
        results  = []
        for owner in owners:
            # 변수에 fk값으로 가져올 항목 참조해서 가져오기
            pets = owner.pet_set.all().values('name', 'age')
            results.append(
               {
                   "name" : owner.name,
                   "age" : owner.age,
                   "email" : owner.email,
                # 리스트 내포 구문으로 가져온 값 넣기...구조에 대해 더 공부하기
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
            # owner의 이름을 넣으려면 어떻게 해야하는지..?
            owner_id = data['owner_id'],
        )
        return JsonResponse({'messasge':'created'}, status=201)  

    def get(self, request):
        pets = Pet.objects.all()
        results = []
        for pet in pets :
            results.append(
                {
                    # pet은 owner를 참조하고 있기 때문에 owner.name으로 가져올 수 있다..
                    "name" : pet.name,
                    "age" : pet.age,
                    "owner": pet.owner.name
                }
            )
        return JsonResponse({'result':results}, status=200)