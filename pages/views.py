from django.shortcuts import render, redirect
from django.views import View
from product.models import Product
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
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
    
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        
        return render(request, 'pages/signup.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
        else:
            return render(request, 'pages/signup.html', {'form': form})
        
class LoginView(View):
    def get(self, request):
        form = LoginForm()

        if request.user.is_authenticated:
            return redirect('index')
        
        else:
            return render(request, 'pages/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('loggedin')
            
            else:
                return render(request, 'pages/login.html', {'form': form, 'error_message' : 'Did not find a match with username/password combination'})
            
        else:
            return render(request, 'pages/login.html', {'form': form})
    
class SuccessLoginView(View):
    def get(self, request):
        return render(request, 'pages/loggedin.html')
    
class LoggedOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        
        else:
            redirect('login')
            
        return render(request, 'pages/loggedout.html')