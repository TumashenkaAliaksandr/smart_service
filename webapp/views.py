from django.shortcuts import render

from webapp.models import *


def index(request):
    main_serv = Services.objects.all()
    brands = Brand.objects.all()

    context = {
        'main_serv': main_serv,
        'brands': brands,
    }

    return render(request, 'webapp/index.html', context=context)


def about(request):
    return render(request, 'webapp/about.html')


def contact(request):
    return render(request, 'webapp/contact.html')


def services(request):
    """Services"""
    main_serv = Services.objects.all()

    context = {
        'main_serv': main_serv,
    }
    return render(request, 'webapp/services.html', context=context)


def shop (request):
    return render(request, 'webapp/shop.html')


def errors(request):
    return render(request, 'webapp/404.html')
