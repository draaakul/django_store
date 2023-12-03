from django.shortcuts import render, HttpResponse
from .models import Products


def index(request):
    return render(request, 'mainpage/index.html')


def about(request):
    return render(request, 'mainpage/about.html')


def detail(request):
    # product = Products.objects.get(id=product_id)
    # context = {
    #     'product': product
    # }
    return render(request, 'mainpage/detail.html')
