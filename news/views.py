from django.shortcuts import render

from news.models import New


def home_page(request):
    news = New.objects.all()
    # tags = Tag.objects.all()
    context = {
        "news": news,
        # "tags":tags,
    }
    return render(request, 'news/index.html', context=context)


def contact_page(request):
    return render(request, 'news/contact.html')


def single_page(request):
    return render(request, 'news/single_page.html')


def page_notfound(request):
    return render(request, 'news/404.html')
