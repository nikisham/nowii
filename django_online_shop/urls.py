from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from shop.views import home_page, nevskiy, kurier, ViewKurier

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls', namespace='accounts')),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('orders/', include('orders.urls', namespace='orders')),
                  path('', home_page, name='home_page'),
                  path('nevkiy/', nevskiy, name='nevskiy'),
                  path('kurier/', kurier, name='kurier'),
                  path('kurier/<int:pk>/', ViewKurier.as_view(), name='view_kurier'),
                  path('shop/', include('shop.urls', namespace='shop',)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
