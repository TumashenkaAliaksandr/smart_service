from django.shortcuts import render

from webapp.models import *


def index(request):

    brands = Brand.objects.all()

    context = locals()

    return render(request, 'webapp/index.html', context)
