from django.shortcuts import render,redirect
from .models import Products,Carts
from django.http import HttpResponse

#it is not a view
def client_ip(request):
    x_f = request.META.get('HTTP_x_f')
    if x_f:
        ip = x_f.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#it is not too
def total_price(carts):
    total = 0
    for cart in carts:
        total += cart.product.price
    return total

def add_to_cart(request,id):
    try:
        product = Products.objects.get(id=id)
        ip = client_ip(request)
        Carts.objects.create(ip=ip,product=product,
                                price=product.price)
        return redirect(request.headers.get('Referer'))
    except Exception as e:
        return HttpResponse(f'Error: {e}')

def products(request):
    products = Products.objects.all()
    context = {
        'prs':products
    }
    return render(request,'./shop.html',context)

def cart_detail(request):
    ip = client_ip(request)
    carts = Carts.objects.filter(ip=ip)
    context = {
        'carts':carts,
        'count':carts.count(),
        'total':total_price(carts)
    }
    return render(request,'./main.html',context)

def del_cart(request,id):
    try:
        cart = Carts.objects.get(pk=id)
        cart.delete()
        return redirect('app1:detail')
    except Exception as e:
        return HttpResponse(f'Error: {e}')