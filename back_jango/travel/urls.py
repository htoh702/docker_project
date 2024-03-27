from django.urls import path,include

from .views import TravelAPI # views파일에 있는 파일의 정보를 가져온다.
from rest_framework import routers

travel_router = routers.DefaultRouter()
travel_router.register(r'api', TravelAPI, basename="cafe_post")


urlpatterns = [
    path('', include(travel_router.urls)),
]