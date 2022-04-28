from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views.decorators.http import require_POST
from django.utils import timezone
from suds.client import Client

from cart.utils.cart import Cart
from orders.forms import CouponForm, Delivery
from orders.models import Order, OrderItem, Coupon


@login_required()
def order_create(request,fio,email,phone,street,home,entrance,floor,flat,description,kurier):
    cart = Cart(request)
    order = Order.objects.create(user=request.user, fio=fio, email=email, phone=phone, street=street, home=home, entrance=entrance, floor=floor, flat=flat, description=description,kurier=kurier)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    cart.clear()
    return redirect('orders:detail', order.id)

@login_required()
def detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = CouponForm()
    return render(request, 'orders/order.html', {'order': order, 'form': form})

@login_required()
def payment(request,order_id, price):
    global amount, o_id
    amount = price
    return redirect('shop:home')

@login_required()
def verify(request):
    order = Order.objects.get(id=o_id)
    order.status = True
    order.save()

@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gt=now, status=True)
        except Coupon.DoesNotExist:
            messages.error(request, 'Такого ПРОМОКОДА не существует', 'danger')
            return redirect('orders:detail', order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount
        order.save()
        return redirect('orders:detail', order_id)
