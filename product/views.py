from django.shortcuts import render
from .models import Product
from django.views import View
from django.core.paginator import Paginator

class ProductView(View):
    electronics = Product.objects.order_by('-date_listed').filter(tag = 'el')
    clothes = Product.objects.order_by('-date_listed').filter(tag = 'cl')
    food = Product.objects.order_by('-date_listed').filter(tag = 'fo')
    other = Product.objects.order_by('-date_listed').filter(tag = 'ot')

    context = {
        'clothes' : clothes,
        'electronics' : electronics,
        'food' : food,
        'other' : other,
    }


    def get(self, request):

        return render(request, 'product/products.html', self.context)