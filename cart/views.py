from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from cart.forms import Add2CartForm
from cart.utils.cart import Cart
from orders.forms import Delivery
from shop.models import Product
from django.views.decorators.http import require_POST


def detail(request):
    cart = Cart(request)
    if request.method == "POST":
        korm = Delivery(request.POST)
        if korm.is_valid():
            fio = korm.cleaned_data['fio']
            email = korm.cleaned_data['email']
            phone = korm.cleaned_data['phone']
            street = korm.cleaned_data['street']
            home = korm.cleaned_data['home']
            entrance = korm.cleaned_data['entrance']
            floor = korm.cleaned_data['floor']
            flat = korm.cleaned_data['flat']
            description = korm.cleaned_data['description']
            kurier = korm.cleaned_data['kurier']
            return redirect('orders:order_create',fio=fio,email=email, phone=phone, street=street, home=home, entrance=entrance, floor=floor, flat=flat, description=description,kurier=kurier)
    else:
        korm = Delivery()
    return render(request, template_name='cart/detail.html', context={'cart': cart, 'korm': korm})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = Add2CartForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        cart.add(product=product, quantity=data['quantity'])
    return redirect('cart:detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')
