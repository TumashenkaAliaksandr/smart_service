import random
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from blog.models import BlogNews
from webapp.models import *



def base(request):

    main_serv = ServicesMain.objects.all()

    context = locals()
    return render(request, 'main/base.html', context)


def index(request):
    main_serv = ServicesMain.objects.all()
    brands = Brand.objects.all()
    favorites = Favors.objects.all()
    main_process = Process.objects.all()
    news = BlogNews.objects.all()

    context = {
        'main_serv': main_serv,
        'brands': brands,
        'favorites': favorites,
        'main_process': main_process,
        'news': news,
    }

    return render(request, 'webapp/index.html', context=context)


def about(request):
    main_serv = ServicesMain.objects.all()
    brands = Brand.objects.all()
    favorites = Favors.objects.all()
    main_process = Process.objects.all()

    context = {
        'main_serv': main_serv,
        'brands': brands,
        'favorites': favorites,
        'main_process': main_process,
    }

    return render(request, 'webapp/about.html', context=context)


def contact(request):
    offices = OfficeContact.objects.all()
    main_serv = ServicesMain.objects.all()
    brands = Brand.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')

        if email and description:
            send_mail(
                subject='Message from your website',
                message=f'Name: {name}\nPhone: {email}\nMessage: {description}',
                from_email='tumashenkaaliaksandr@gmail.com',
                recipient_list=['Badminton500@inbox.lv'],  # Замените на ваш адрес получателя
                fail_silently=False,
            )

            return render(request, 'webapp/success.html')  # Шаблон для страницы успешной отправки

    context = {
        'main_serv': main_serv,
        'brands': brands,
        'offices': offices,
    }

    return render(request, 'webapp/contact.html', context=context)  # Шаблон с формой обратной связи


def services(request):
    """Services"""
    main_serv = ServicesMain.objects.all()
    brands = Brand.objects.all()
    favorites = Favors.objects.all()

    context = {
        'main_serv': main_serv,
        'brands': brands,
        'favorites': favorites,
    }
    return render(request, 'webapp/services/services.html', context=context)


def shop(request):
    return render(request, 'webapp/services/shop.html')


def encoders(request):
    main_serv = ServicesMain.objects.all()
    main_encoders = Shop_Encoders.objects.all()
    brands = Brand.objects.all()

    context = {
        'main_serv': main_serv,
        'main_encoders': main_encoders,
        'brands': brands,
    }
    return render(request, 'webapp/services/shop-encoders.html', context=context)


def board(request):
    main_serv = ServicesMain.objects.all()
    main_board = Shop_Board.objects.all()
    brands = Brand.objects.all()

    context = {
        'main_serv': main_serv,
        'main_board': main_board,
        'brands': brands,
    }
    return render(request, 'webapp/services/services-board.html', context=context)


def inverter(request):
    main_serv = list(ServicesMain.objects.all())
    random.shuffle(main_serv)  # Перемешиваем список объектов
    main_inverter = Shop_Inverter.objects.all()
    brands = Brand.objects.all()

    context = {
        'main_serv': main_serv,
        'main_inverter': main_inverter,
        'brands': brands,
    }
    return render(request, 'webapp/services/services-inverter.html', context=context)

def bcm(request):
    main_serv = list(ServicesMain.objects.all())
    random.shuffle(main_serv)  # Перемешиваем список объектов
    main_bcm = Shop_Inverter.objects.all()
    brands = Brand.objects.all()

    context = {
        'main_serv': main_serv,
        'main_inverter': main_bcm,
        'brands': brands,
    }
    return render(request, 'webapp/services/services_bcm.html', context=context)

def electro_transport(request):
    main_serv = list(ServicesMain.objects.all())
    random.shuffle(main_serv)  # Перемешиваем список объектов
    main_el_trans = Shop_Inverter.objects.all()
    brands = Brand.objects.all()

    context = {
        'main_serv': main_serv,
        'main_inverter': main_el_trans,
        'brands': brands,
    }
    return render(request, 'webapp/services/electro_transport.html', context=context)


def indastrial_electroniks(request):
    main_inverter = Shop_Indastrial_Electroniks.objects.all()
    brands = Brand.objects.all()
    main_serv = list(ServicesMain.objects.all())
    random.shuffle(main_serv)  # Перемешиваем список объектов

    context = {
        'main_serv': main_serv,
        'main_inverter': main_inverter,
        'brands': brands,
    }
    return render(request, 'webapp/services/industrial-electronics.html', context=context)


def cpc_four(request):
    main_serv = list(ServicesMain.objects.all())
    random.shuffle(main_serv)  # Перемешиваем список объектов
    main_cpc_four = BlockCpcFour.objects.all()
    brands = Brand.objects.all()

    context = {
        'main_serv': main_serv,
        'main_cpc_four': main_cpc_four,
        'brands': brands,
    }
    return render(request, 'webapp/services/blocks/cpc4.html', context=context)


def errors(request):
    return render(request, 'webapp/404.html')

def success(request):
    return render(request, 'webapp/success.html')


def game_repair(request):
    return render(request, 'webapp/team.html')
