from django import forms

from orders.models import Order


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class Delivery(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    fio = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(label='Улица', widget=forms.TextInput(attrs={'class': 'form-control'}))
    home = forms.CharField(label='Дом', widget=forms.TextInput(attrs={'class': 'form-control'}))
    entrance = forms.CharField(label='Подъезд', widget=forms.TextInput(attrs={'class': 'form-control'}))
    floor = forms.CharField(label='Этаж', widget=forms.TextInput(attrs={'class': 'form-control'}))
    flat = forms.CharField(label='Квартира', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Коментарий', widget=forms.Textarea(attrs={'class': 'form-control'}))
    kurier = forms.ChoiceField(choices=Order.CHO_KUR, widget=forms.Select(attrs={'class': 'form-control'}))
