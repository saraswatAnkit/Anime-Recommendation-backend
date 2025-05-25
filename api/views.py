from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from .utils import search_anime
from rest_framework.permissions import IsAuthenticated
from .models import UserPreference
import logging
logger = logging.getLogger('api')

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        logger.info(f"Registering user with data: {request.data}")
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def anime_search(request):
    name = request.GET.get('name')
    genre = request.GET.get('genre')
    data = search_anime(query=name, genre=genre)
    logger.info(f"Search results for name: {name}, genre: {genre} - {data}")
    return Response(data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_preferences(request):
    user = request.user
    if request.method == 'POST':
        genres = request.data.get('favorite_genres')
        obj, created = UserPreference.objects.update_or_create(user=user, defaults={'favorite_genres': genres})
        logger.info(f"User {user.username} updated preferences: {genres}")
        return Response({'message': 'Preferences updated'})
    else:
        try:
            pref = UserPreference.objects.get(user=user)
            return Response({'favorite_genres': pref.favorite_genres})
        except UserPreference.DoesNotExist:
            return Response({'message': 'No preferences set'}, status=400)
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def anime_recommendations(request):
    try:
        pref = UserPreference.objects.get(user=request.user)
        genres = pref.favorite_genres.split(',')
        logger.info(f"User {request.user.username} preferences: {genres}")
        data = []
        for genre in genres:
            genre = genre.strip()
            result = search_anime(genre=genre.strip())
            print(f"API Respone {genre}: {result}")
            data.extend(result['data']['Page']['media'])
        return Response(data[:10])
    except UserPreference.DoesNotExist:
        return Response({'message': 'No preferences set'}, status=404)