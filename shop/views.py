from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import DetailView

from cart.forms import Add2CartForm
from shop.forms import ContactUs, ContactUsForm
from shop.models import Product, Category, Kurier


def nevskiy(request):
    return render(request, 'newsk_r.html', {})

class ViewKurier(DetailView):
    model = Kurier

def kurier(request):
    kurier = Kurier.objects.all()
    return render(request, 'shop/kurier.html', {'kurier': kurier})


def home_page(request):
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = ContactUs()

    return render(request, 'home_page.html', {'form': form})


def home(request, slug=None):
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    else:
        form = ContactUs()
    products = Product.objects.filter(status=True)

    category = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html', {'products': products, 'category': category, 'form': form})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = Add2CartForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})
