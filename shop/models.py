from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True,
                                     blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('shop:category_filter', args={self.slug})


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%b/%d/')
    description = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('shop:product_detail', args={self.slug, })

class Contact(models.Model):
    name = models.TextField(max_length=150, verbose_name='Имя')
    email = models.TextField(max_length=150,verbose_name='Email')
    phone = models.TextField(max_length=150, verbose_name='Телефон')
    message = models.TextField(verbose_name='Начало')
    is_processed = models.BooleanField(default=False, blank=True, verbose_name='Обработан?')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

class Kurier(models.Model):
    name = models.TextField(max_length=150, verbose_name='Имя')
    desc = models.TextField(max_length=150, verbose_name='Описание')
    img = models.ImageField(verbose_name='Картинка',upload_to="photos/kurier",blank=True)

    def get_absolute_url(self):
        return reverse('view_kurier', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'