from django import forms

from shop.models import Contact


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message', 'is_processed')

class ContactUs(ContactUsForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control'}))
