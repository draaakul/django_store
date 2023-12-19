from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Products


def index(request):
    data = Products.objects.all()
    context = {
        'products': data,
    }
    return render(request, 'mainpage/index.html', context=context)


def about(request):
    return render(request, 'mainpage/about.html')


def detail(request):
    # product = Products.objects.get(id=product_id)
    # context = {
    #     'product': product
    # }
    return render(request, 'mainpage/detail.html')
