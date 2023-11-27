from django.shortcuts import render, redirect
from django.views import View
from product.models import Product
from time import sleep

class IndexView(View):
    featured_product = Product.objects.order_by('-date_listed').filter(currently_listed=True)[0]
    clothes_products = Product.objects.order_by('-date_listed').filter(tag='cl')[:3]
    
    context = {
        'featured_product' : featured_product,
        'clothes_products' : clothes_products,
    }

    def get(self, request):
        return render(request, 'pages/index.html', self.context)