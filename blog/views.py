from blog.models import *
from django.shortcuts import render

from webapp.models import ServicesMain


def blog(request):
    """these are views for Blog News list"""
    model_blog_main = BlogNews.objects.all()
    news_for_footer = BlogNews.objects.all()[:2]
    news = BlogNews.objects.all()
    our_services = ServicesMain.objects.all()

    context = locals()
    return render(request, 'blog/blog.html', context=context)


def blog_news(request, pk):
    """these are views for Blog News list"""
    news = BlogNews.objects.filter(pk=pk)

    context = {
        'news': news,
    }
    return render(request, 'blog/blog.html', context=context)


def NewsDetailView(request, pk):
    """Views for News details"""
    news = BlogNews.objects.filter(pk=pk)
    news_blog_main = BlogNews.objects.all()
    our_services = ServicesMain.objects.all()

    context = {
        'news': news,
        'news_blog_main': news_blog_main,
        'our_services': our_services,
    }
    return render(request, 'blog/blog-single.html', context=context)



