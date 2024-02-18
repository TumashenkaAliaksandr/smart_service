import random
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from webapp.models import *



def base(request):

    main_serv = Services.objects.all()

    context = locals()
    return render(request, 'main/base.html', context)


def index(request):
    main_serv = Services.objects.all()
    brands = Brand.objects.all()
    favorites = Favors.objects.all()

    context = {
        'main_serv': main_serv,
        'brands': brands,
        'favorites': favorites,
    }

    return render(request, 'webapp/index.html', context=context)


def about(request):
    main_serv = Services.objects.all()

    context = {
        'main_serv': main_serv,
    }
    return render(request, 'webapp/about.html', context=context)


def contact(request):

    main_serv = Services.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')

        if email and description:
            send_mail(
                subject='Message from your website',
                message=f'Name: {name}\nEmail: {email}\nMessage: {description}',
                from_email='tumashenkaaliaksandr@gmail.com',
                recipient_list=['Badminton500@inbox.lv'],  # Замените на ваш адрес получателя
                fail_silently=False,
            )

            return render(request, 'webapp/success.html')  # Шаблон для страницы успешной отправки

    context = {
        'main_serv': main_serv,
    }

    return render(request, 'webapp/contact.html', context=context)  # Шаблон с формой обратной связи


def services(request):
    """Services"""
    main_serv = Services.objects.all()

    context = {
        'main_serv': main_serv,
    }
    return render(request, 'webapp/services/services.html', context=context)


def shop(request):
    return render(request, 'webapp/services/shop.html')


def shop_encoders(request):
    main_serv = Services.objects.all()
    main_encoders = Shop_Encoders.objects.all()

    context = {
        'main_serv': main_serv,
        'main_encoders': main_encoders,
    }
    return render(request, 'webapp/services/shop-encoders.html', context=context)


def shop_board(request):
    main_serv = Services.objects.all()
    main_board = Shop_Board.objects.all()

    context = {
        'main_serv': main_serv,
        'main_board': main_board,
    }
    return render(request, 'webapp/services/services-board.html', context=context)


def shop_inverter(request):
    main_serv = list(Services.objects.all())
    random.shuffle(main_serv)  # Перемешиваем список объектов
    main_inverter = Shop_Inverter.objects.all()

    context = {
        'main_serv': main_serv,
        'main_inverter': main_inverter,
    }
    return render(request, 'webapp/services/services-inverter.html', context=context)


def errors(request):
    return render(request, 'webapp/404.html')

def success(request):
    return render(request, 'webapp/success.html')


def game_repair(request):
    return render(request, 'webapp/game-repair.html')
