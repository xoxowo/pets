
from xml.etree.ElementInclude import include
from django.urls import path, include

urlpatterns = [
    # 내가 정의한 앱의 urls 를 넣어줘야함 
    path('member', include('member.urls')),
    path('movies', include('movies.urls')),
    path('pizza', include('pizza.urls')),
    
]
