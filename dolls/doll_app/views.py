from django.shortcuts import render
from .models import Dolls, Photo
from basket.forms import BasketAddProductForm


def interior_dolls_list(request):
    dolls = Dolls.objects.filter(type='Интерьерные куколки')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)


def for_game_list(request):
    dolls = Dolls.objects.filter(type='Игровые куколки')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)


def toys_list(request):
    dolls = Dolls.objects.filter(type='Игрушки')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)


def doll_wear(request):
    dolls = Dolls.objects.filter(type='Одежда для кукол')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)


def toy_wear(request):
    dolls = Dolls.objects.filter(type='Одежда для игрушек')
    context = {
        'dolls': dolls
    }
    return render(request, 'dolls_list.html', context)


def doll_detail(request, pk):
    doll = Dolls.objects.get(pk=pk)
    photos = Photo.objects.filter(dolls=doll)
    basket_product_form = BasketAddProductForm()
    context = {
        'doll': doll,
        'photos': photos,
        'basket_product_form': basket_product_form
    }
    return render(request, 'doll_detail.html', context)
