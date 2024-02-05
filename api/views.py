from rest_framework import viewsets, status
from rest_framework.decorators import action 
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, create = Token.objects.get_or_create(user=serializer.instance)
        return Response({
            'token':token.key,
        },
            status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        response = {'message': "Not Allowd" }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, *args, **kwargs):
        response = {'message': "Not Allowd" }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, *args, **kwargs):
        response = {'message': "Not Allowd" }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, *args, **kwargs):
        response = {'message': "Not Allowd" }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication, ) 
    permission_classes = (IsAuthenticated, )

    # rating meals 
    @action(detail=True ,methods=['post'] )
    def rate_meal(self, request, pk=None): 
        if 'stars' in request.data: 
            '''
                create or updata
            '''
            meal = Meal.objects.get(id=pk) 
            stars = request.data['stars'] 
            user = request.user
            
            # username = request.data['username'] 
            # user = User.objects.get(username=username) 
            try: 
                # update 
                rating = Rating.objects.get(meal=meal, user=user.id)
                rating.stars = stars 
                rating.save() 
                serializer =RatingSerializer(rating, many=False) 

                json = {
                    'message' : 'Meal reting Updated',
                    'serializer': serializer.data,
                }
                return Response(json, status=status.HTTP_202_ACCEPTED)
            except: 
                # create 
                rating = Rating.objects.create(stars=stars, user=user, meal=meal)
                serializer = RatingSerializer(rating, many=False) 
                json = {
                    'message': 'Rating is Created', 
                    'serilizer': serializer.data 
                }
                return Response(json, status=status.HTTP_200_OK)
        else: 
            json={
                'message': 'stars not provided',
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)






class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, ) 
    permission_classes =  (IsAuthenticated, ) 

    def update(self, request, *args, **kwargs): 
        response = { 
            'message': 'Invalid way to create or update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 
    
    def create(self, request, *args, **kwargs): 
        response = { 
            'message': 'Invalid way to create or update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 
    
