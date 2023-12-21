from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product


def index(request):
    products_data = Product.objects.all()
    context = {
        'mainpage_products': products_data[:8],
        'all_products': products_data,
        'popular_products': products_data[:4],
        'my_range': range(5),

    }
    return render(request, 'mainpage/index.html', context=context)


def about(request):
    return render(request, 'mainpage/about.html')


def detail(request, detail_slug):
    slug_detail = get_object_or_404(Product, slug=detail_slug)

    data = {
        'product': slug_detail,
    }
    return render(request, 'mainpage/detail.html', context=data)
