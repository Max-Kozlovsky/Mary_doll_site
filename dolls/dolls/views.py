from django.shortcuts import render, redirect
from .forms import Order
from doll_app.models import Dolls
from telebot import TeleBot
from dolls.settings import TELEGRAM_BOT_API_KEY, telegram_chat_id


def main(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def after_order(request):
    return render(request, 'after_order.html')


def send_order(request, pk):
    doll = Dolls.objects.get(pk=pk)
    form = Order(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        city = form.cleaned_data['city']
        address = form.cleaned_data['address']
        phone = form.cleaned_data['phone']
        if len(name + city + address + phone) > 0:
            bot = TeleBot(TELEGRAM_BOT_API_KEY)
            bot.send_message(telegram_chat_id, f"Заказ куклы {doll.name}.\n"
                                               f"Данные заказчика:\n"
                                               f"ФИО: {name}, \n"
                                               f"Адрес: {city + ' ' + address},\n"
                                               f"Контактный телефон: {phone}")
            return redirect('after_order')
    else:
        form = Order()
    context = {
        'doll': doll,
        'form': form,
    }
    return render(request, 'order.html', context)
