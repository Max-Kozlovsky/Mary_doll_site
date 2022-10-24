from django.conf import settings
from doll_app.models import Dolls


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.CART_SESSION_ID)
        if not basket:
            basket = self.session[settings.CART_SESSION_ID] = {}
        self.basket = basket

    def add(self, doll, count=1, update_count=False):
        doll_id = str(doll.id)
        if doll_id not in self.basket:
            self.basket[doll_id] = {
                'id': doll.id,
                'name': doll.name,
                'count': 0,
                'price': int(doll.price),
                'image': str(doll.image)
            }
        if update_count:
            self.basket[doll_id]['count'] = count
        else:
            self.basket[doll_id]['count'] += count
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.basket
        self.session.modified = True

    def remove(self, doll):
        doll_id = str(doll.id)
        if doll_id in self.basket:
            del self.basket[doll_id]
            self.save()

    def __iter__(self):
        doll_ids = self.basket.keys()
        dolls = Dolls.objects.filter(id__in=doll_ids)
        for doll in dolls:
            self.basket[str(doll.id)][doll] = doll

        for item in self.basket.values():
            doll_price = int(item['price'])
            item['price'] = int(doll_price)
            item['total_price'] = doll_price * item['count']
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.basket.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(item['price'] * int(item['count']) for item in self.basket.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
