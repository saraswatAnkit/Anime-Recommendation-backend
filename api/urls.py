from django.urls import path
from .views import anime_search, user_preferences, anime_recommendations 

urlpatterns = [
    path('anime/search/', anime_search),
    path('anime/recommendations/', anime_recommendations),
    path('user/preferences/', user_preferences),
]