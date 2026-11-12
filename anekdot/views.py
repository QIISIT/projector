from django.shortcuts import get_object_or_404, redirect, render
from .models import  Product, Order
from datetime import timedelta
from django.utils import timezone

def rezero(request):
    week_ago = timezone.now() - timedelta(days=7)
    products = Product.objects.filter(created_at__gte=week_ago)  # только новинки
    orders = Order.objects.all()
    return render(request, 'catalog-time.html', {'products': products, 'orders': orders})

def index(request):
    order = Order.objects.all()
    product = Product.objects.all()
    return render(request, 'catalog.html', {'products': product, 'orders': order})

def product(request, id):
    product = get_object_or_404(Product, pk=id)
    orders = product.orders.select_related('product').all()
    return render(request, 'order.html', {'product': product, 'orders': orders})

def buy(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product.bought = True
        product.save()
    return redirect(f'/product/{id}/')

