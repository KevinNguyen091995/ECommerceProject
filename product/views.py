from django.shortcuts import render
from .models import Product
from django.views import View

class ProductView(View):
    def get(self, request):
        return render(request, 'pages/index.html', self.context)