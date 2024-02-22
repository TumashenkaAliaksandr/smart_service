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
    path('encoders/', encoders, name='encoders'),
    path('board/', board, name='board'),
    path('inverter/', inverter, name='inverter'),
    path('errors/', errors, name='errors'),
    path('success/', success, name='success'),
    path('game_repair/', game_repair, name='game_repair'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
