from django.shortcuts import render
from .models import Product
from promotions.models import Promotion
from reviews.models import Review


def home(request):
    products = Product.objects.all()
    promotions = Promotion.objects.filter(active=True)

    return render(request, 'shop/home.html', {
        'products': products,
        'promotions': promotions
    })
