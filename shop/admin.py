import var_dump
from django.contrib import admin

# Register your models here.
from shop.forms import ContactUs
from shop.models import Category, Product, Contact, Kurier


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('status', 'created')
    list_editable = ('price', 'status')
    raw_id_fields = ('category',)
    actions = ('change_status',)

class ContactAdmin(admin.ModelAdmin):
    form = ContactUs
    model = Contact
    list_display = ('id', 'name', 'is_processed')
    list_display_links = ('id', 'name', 'is_processed')

class KurierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Kurier, KurierAdmin)

    # change_status.short_description = 'change status .'
