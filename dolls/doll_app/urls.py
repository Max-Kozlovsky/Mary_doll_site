from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('interior_dolls_list', views.interior_dolls_list, name='interior_dolls_list'),
    path("dolls_detail/<int:pk>/", views.doll_detail, name='doll_detail'),
    path('for_game_dolls_list', views.for_game_list, name='for_game_dolls_list'),
    path('toys_list', views.toys_list, name='toys_list'),
]
