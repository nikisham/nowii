from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from shop.models import Product, Kurier


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True, default=None)
    fio = models.CharField(max_length=100, blank=True, null=True, default=None)
    email = models.EmailField(max_length=100,blank=True, null=True, default=None)
    phone = models.CharField(max_length=100,blank=True, null=True, default=None)
    kurier = models.ManyToManyField(Kurier)
    street = models.CharField(max_length=100,blank=True, null=True, default=None)
    home = models.CharField(max_length=100,blank=True, null=True, default=None)
    entrance = models.CharField(max_length=100,blank=True, null=True, default=None)
    floor = models.CharField(max_length=100,blank=True, null=True, default=None)
    flat = models.CharField(max_length=100,blank=True, null=True, default=None)
    description = models.TextField(default='')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.user} - {self.id}"

    @property
    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'
