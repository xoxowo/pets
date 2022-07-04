from django.urls import URLPattern, path
from member.views import OwnerView, PetView

urlpatterns = [
    path('/owner', OwnerView.as_view()),
    path('/pet', PetView.as_view())
]