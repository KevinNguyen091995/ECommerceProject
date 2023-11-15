from django.shortcuts import render
from django.views import View
from product.models import Product

class IndexView(View):
    featured_products = Product.objects.order_by('-date_listed').filter(currently_listed=True)[:3]
    
    context = {
        'featured_products' : featured_products,
    }

    def get(self, request):
        return render(request, 'pages/index.html', self.context)