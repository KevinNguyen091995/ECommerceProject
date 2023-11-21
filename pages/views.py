from django.shortcuts import render, redirect
from django.views import View
from product.models import Product
from django.contrib.auth.models import User
from .forms import SignUpForm

class IndexView(View):
    featured_product = Product.objects.order_by('-date_listed').filter(currently_listed=True)[0]
    clothes_products = Product.objects.order_by('-date_listed').filter(tag='cl')[:3]
    
    context = {
        'featured_product' : featured_product,
        'clothes_products' : clothes_products,
    }

    def get(self, request):
        return render(request, 'pages/index.html', self.context)
    
class LoginView(View):
    def get(self, request):
        return render(request, 'pages/login.html')
    
class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        
        return render(request, 'pages/signup.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            print("SAVED TO DB")

            return redirect('login')
        
        else:
            # Form is not valid, render the form with errors
            return render(request, 'pages/signup.html', {'form': form})