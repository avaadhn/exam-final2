from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('products',views.products,name='products'),
    path('carts',views.cart_detail,name='detail'),
    path('add_cart/<id>',views.add_to_cart,name='add_cart'),
    path('del-cart/?id=<id>',views.del_cart,name='del_cart')
]
