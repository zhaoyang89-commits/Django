from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.game_list, name='game_list'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('games/add/', views.add_game, name='add_game'),
    path('games/<int:game_id>/delete/',views.delete_game,name='delete_game')
]