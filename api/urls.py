from django.urls import path, include 
from rest_framework import routers 
from .views import MealViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('maels',MealViewSet) 
router.register('ratings', RatingViewSet) 


urlpatterns = [
    path('', include(router.urls))
]


