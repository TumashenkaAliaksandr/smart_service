from django.shortcuts import render

from webapp.models import *


def index(request):

    brands = Brand.objects.all()

    context = locals()

    return render(request, 'webapp/index.html', context)


def about(request):

    return render(request, 'webapp/about.html')

def contact(request):

    return render(request, 'webapp/contact.html')