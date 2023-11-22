from django.shortcuts import render
from .models import Product
from django.views import View

class ProductView(View):
    electronics = Product.objects.order_by('-date_listed').filter(tag = 'el')
    clothes = Product.objects.order_by('-date_listed').filter(tag = 'cl')
    food = Product.objects.order_by('-date_listed').filter(tag = 'fo')
    other = Product.objects.order_by('-date_listed').filter(tag = 'ot')

    context = {
        'electronics' : electronics,
        'clothes' : clothes,
        'food' : food,
        'other' : other
    }

    def get(self, request):
        return render(request, 'product/products.html', self.context)