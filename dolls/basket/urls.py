from django.urls import path, re_path
from . import views


urlpatterns = [
    path('basket_clear', views.basket_clear, name='basket_clear'),
    re_path(r'^$', views.basket_detail, name='basket_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.basket_add, name='basket_add'),
    re_path(r'^remove/(?P<doll_id>\d+)/$', views.basket_remove, name='basket_remove'),

]
