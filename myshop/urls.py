from django.contrib import admin 
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('', include('shop.urls', namespace='shop')),
    path('orders/', include('orders.urls', namespace='orders')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
