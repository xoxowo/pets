import json

from django.http import JsonResponse
from django.views import View

from member.models import Owner, Pet

class OwnerView(View):
    """
    목적 : 주인의 정보를 데이터베이스에 저장
    1. client에게 주인의 정보를 받는다.
    2. 받은 정보를 데이터 베이스에 저장
    3. 단순한 형태 코드를 먼저 만들고 그 다음에 추가로 코드 작업하기..
    4. 저장하는 것은 post method로 만든다. class 에서 만드는 함수니까 self를 인자로 받음
    """
    def post(self, request):
        """
        클라이언트가 주는 정보 body 예상해보기
        프론트가 주는 키와 내 키가 일치할 수 있도록 맞춰야함 
        request.body = {
        "name": "ddd", 
        "email" : "ddd@naver.com",
        "age" : 22
        }
        """
        data = json.loads(request.body)
        Owner.objects.create(
            name = data['name'], #  <- 왼쪽은 우리가 모델에 정의한 속성값 / 오른쪽은 속성에 넣을 값
            age = data['age'],
            email = data['email'],
        )
        #   메세지는 프론트가 보는 값 / 데이터를 생성할때 코드는 201 
        return JsonResponse({'messasge':'created'}, status=201)    

    def get(self, request):
        # owner의 모든 정보를 변수에 넣기
        owners = Owner.objects.all()
        # 빈 리스트 만들어서 for 문으로 owner 정보를 한개씩 넣어주기 append.({딕셔너리 방식으로!})
        results  = []
        for owner in owners:
            # 변수에 fk값으로 가져올 항목 참조해서 가져오기
            #   _set.all() 역참조를 해서 펫의 정보를 역으로 가져옴 아래는 이런 형식 (주인입장에서는 펫의 정보를 모르기 때문에 역으로 참조한다. 역참조.)
            # related_name= 으로 가져올 수 있음. 
            pets = owner.pet_set.all().values('name', 'age')  # Pet.objects.filter(owner=owner)와 같은 효과
            # QuerySet [Pet1, Pet2, ...]
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
    """
    목적 : pet에 대한 정보를 db에 저장
    1. 클라이언트로 부터 pet에 대한 정보를 받음
        - pet이름
        - 나이
        - 주인의 정보
    2. 받은 정보를 orm을 이용해 저장
    """
    def post(self, request):
    # try : 오너의 ㅈ정보가 없으면 저장이안되니까 꼭 예외처리 해줘야함...

        data = json.loads(request.body)
    #   데이터를 먼저 검증한 후에 하는게 좋다.    
    #   if not Owner.objects.filter(id=owner_id).exitst() :
    #       return JsonResponse({'messasge':'Not Found'}, status=404)
        Pet.objects.create(
            name = data['name'],
            age = data['age'],
            # owner의 이름을 넣으려면 어떻게 해야하는지..?
            owner_id = data['owner_id'],
            # owner = owner
        )
        return JsonResponse({'messasge':'created'}, status=201)  
    # except Owner.DoseNotExist : -> owner = Owner.objects.get(id=data['owner']) 이 코드에서 나는 예외처리
        # return JsonResponse({'messasge':'Not Found'}, status=404)
    # except KeyError : 500 error 는 백앤드에서 예외처리를 안한 거라... 꼭 처리해줘야함
        # return JsonResponse({'messasge':'Key Error'}, status=400)
            
    def get(self, request):
        """
        목적 : pet의 정보를 데이터베이스로부터 가져와서 전달
        
        1. 데이터베이스에서 pet의 정보를 모두 가져온다.
        2. 가져온 데이터를 json으로 보낼 수 있도록 가공한다. (객체를 json으로 바로 보낼 수 없어 객체를 ->dict로 변환해서 보내야함)
        3. 가공한 데이터를 전달한다.
        """
        # 1. pet의 정보를 모두 가져온다. 복수로 이름을 저장하는 것이 좋다
        pets = Pet.objects.all()
        #  빈리스트에 정보를 담아 전달
        results = []
        # 객체 하나하나를 pet 변수에 할당하고 값을 뽑아냄.
        for pet in pets :
            """
            이렇게 담을 딕셔너리 를 만들고 여기에 넣어도 된다.
            pet_info = {
                "name" : pet.name,
                "age" : pet.age,
                "owner": pet.owner.name
            }        
            results.append(pet_info)
            """
            results.append(
                {
                    # pet은 owner를 참조하고 있기 때문에 owner.name으로 가져올 수 있다..
                    "name" : pet.name,
                    "age" : pet.age,
                    # 주인의 이름을 가져오기 위해 pet class에 owner라는 속성이있고 foreingkey로 owner 클래스의 속성인 name을 가져올 수 있었다.
                    "owner": pet.owner.name
                }
            )
        return JsonResponse({'result':results}, status=200)