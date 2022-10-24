from django.shortcuts import render, redirect
from .forms import Order
from telebot import TeleBot
from dolls.settings import TELEGRAM_BOT_API_KEY, telegram_chat_id
from basket.basket import Basket


def main(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def after_order(request):
    return render(request, 'after_order.html')


def send_order(request):
    basket = Basket(request)
    order_list = [str(value) for item in basket for key, value in item.items() if key == 'name' or key == 'count']
    form = Order(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        city = form.cleaned_data['city']
        address = form.cleaned_data['address']
        phone = form.cleaned_data['phone']
        info = form.cleaned_data['info']
        if len(name + city + address + phone) > 0:
            bot = TeleBot(TELEGRAM_BOT_API_KEY)
            bot.send_message(telegram_chat_id, f"Заказ куклы {(' '.join(order_list))}.\n"
                                               f"Общая стоимость заказа: {basket.get_total_price()} рублей\n"
                                               f"Данные заказчика:\n"
                                               f"ФИО: {name}, \n"
                                               f"Адрес: {city + ' ' + address},\n"
                                               f"Контактный телефон: {phone}\n"
                                               f"Информация от заказчика: {info}")
            basket.clear()
            return redirect('after_order')
    else:
        form = Order()
    context = {
        'form': form,
    }
    return render(request, 'order.html', context)


def not_found(request):
    return render(request, '404.html')
