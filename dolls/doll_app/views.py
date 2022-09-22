from django.shortcuts import render
from .models import Dolls, Photo

"""_________________________________Interior Dolls___________________________________________________________________"""


def interior_dolls_list(request):
    dolls = Dolls.objects.filter(type='Интерьерные куколки')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)


def doll_detail(request, pk):
    doll = Dolls.objects.get(pk=pk)
    photos = Photo.objects.filter(category=doll)
    context = {
        'doll': doll,
        'photos': photos
    }
    return render(request, 'doll_detail.html', context)


"""-------------------------------Game dolls-------------------------------------------------------------------------"""


def for_game_list(request):
    dolls = Dolls.objects.filter(type='Игровые куколки')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)


"""--------------------------------------Toys------------------------------------------------------------------------"""


def toys_list(request):
    dolls = Dolls.objects.filter(type='Игрушки')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)
