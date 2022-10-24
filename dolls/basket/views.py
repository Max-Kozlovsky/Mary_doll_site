from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from doll_app.models import Dolls
from .forms import BasketAddProductForm
from .basket import Basket


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    doll = get_object_or_404(Dolls, id=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(doll=doll,
                   count=cd['count'],
                   update_count=cd['update'])
    return redirect('basket:basket_detail')


def basket_remove(request, doll_id):
    basket = Basket(request)
    doll = get_object_or_404(Dolls, id=doll_id)
    basket.remove(doll)
    return redirect('basket:basket_detail')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket.html', {'basket': basket})


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'basket.html')
