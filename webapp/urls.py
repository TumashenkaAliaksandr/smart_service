from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('shop/', shop, name='shop'),
    path('shop_encoders/', shop_encoders, name='shop_encoders'),
    path('shop_board/', shop_board, name='shop_board'),
    path('shop_inverter/', shop_inverter, name='shop_inverter'),
    path('errors/', errors, name='errors'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
