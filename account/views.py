from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from .forms import SignUpForm, LoginForm
from .models import AccountAvatar
from product.models import Product

class AccountDetailView(View):
    template_name = 'account/profile_view.html'
    
    def get(self, request, username):
        print(username)

        # Checked Login Profile View
        if request.user.is_authenticated:
            current_user = User.objects.filter(username = username).get()
            current_user_avatar = AccountAvatar.objects.filter(user = current_user.id).get()
            total_products = len(Product.objects.filter(seller = current_user.id))

            context = {
                'current_user' : current_user,
                'current_user_avatar' : current_user_avatar,
                'total_products' : total_products
                }
            
            return render(request, self.template_name, context)
        
        else:
            return redirect('login')

class SignUpView(View):
    template_name = 'account/sign_up.html'

    def get(self, request):
        # Generate Registration Form
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            # Gather Input and Save user to DB
            user = form.save(commit=False)
            user.save()

            #Create Profile with Defaulted Icon
            AccountAvatar.objects.create(user=user)
            return redirect('login')
        
        else:
            return render(request, self.template_name, {'form': form})
        
class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        form = LoginForm()

        if request.user.is_authenticated:
            return redirect('index')
        
        else:
            return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            #Authenticate Username/Password Inputted
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                #Login User
                login(request, user)
                return redirect('loggedin')
            
            else:
                return render(request, self.template_name, {'form': form, 'error_message' : 'Did not find a match with username/password combination'})
            
        else:
            return render(request, self.template_name, {'form': form})
    
class SuccessLoginView(View):
    template_name = 'account/logged_in.html'

    def get(self, request):
        # Successful Login
        if request.user.is_authenticated:
            return render(request, self.template_name)
        
        else:
            return redirect('login')
    
class LoggedOutView(View):
    template_name = 'account/logged_out.html'

    def get(self, request):
        # Successful Logout
        if request.user.is_authenticated:
            logout(request)
        
        else:
            return redirect('login')
            
        return render(request, self.template_name)