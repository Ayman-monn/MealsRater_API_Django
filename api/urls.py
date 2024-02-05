from django.urls import path, include 
from rest_framework import routers 
from rest_framework.authtoken.views import obtain_auth_token
from .views import MealViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet) 
router.register('maels',MealViewSet) 
router.register('ratings', RatingViewSet) 


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]


