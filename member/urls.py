from django.urls import URLPattern, path
from member.views import OwnerView, PetView

urlpatterns = [

    #프로젝트 urls에 있는 스트링과 여기에 있는 더하기 때문에 만약 둘다 /owner /owner 이면 합쳐진 :8000/owner/owner 이렇게 접속됨
    path('/owner', OwnerView.as_view()),
    path('/pet', PetView.as_view()),
]