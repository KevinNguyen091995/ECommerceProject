from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import SignUpForm, LoginForm, RateUserForm
from .models import AccountAvatar, VerifiedUser, UserRating
from product.models import Product


def AccountDetailView(request, username):
    form = RateUserForm()

    # User Model
    current_user = User.objects.filter(username = username).get()
    current_user_avatar = AccountAvatar.objects.filter(user = current_user.id).get()

    # Product
    total_products = len(Product.objects.filter(seller = current_user.id))
    account_product = Product.objects.order_by('-date_listed')[:3]

    # Reviews
    reviews = UserRating.objects.order_by('-date_reviewed').filter(user = current_user.id)[:5]

    # Checks
    reviewed_before = UserRating.objects.filter(rated_user = request.user.id, user = current_user.id).exists()
    not_same_user = current_user.id != request.user.id

    context = {
    'current_user' : current_user,
    'current_user_avatar' : current_user_avatar,
    'total_products' : total_products,
    'reviews' : reviews,
    'account_product' : account_product,
    } 

    # Add form to profile view if not same user and allows to comment/rate
    if not_same_user:
        context.update({'form' : form})

    if request.method == 'POST' and not_same_user:
        form = RateUserForm(request.POST)

        # Check If User is Logged In
        if request.user.is_authenticated == False:
            return render(request, 'account/login.html', {'error_message' : 'Need to login to rate a user'})
        
        #Check Double Review
        if reviewed_before:
            context.update({'error_message' : 'Already reviewed this user, cannot review again.'})
            return render(request, 'account/account_view.html', context)

        # Check if POST is valid 1-5 rating and form is valid
        if form.is_valid() and form.cleaned_data['rating'] > 0 and form.cleaned_data['rating'] <= 5:
            form.instance.user = current_user
            form.instance.rated_user_id = request.user.id
            form.save()
            return render(request, 'account/account_view.html', context)
        
        
        else:
            context.update({'error_message' : 'Invalid Rating, please ensure both fields are selected/filled'})
            return render(request, 'account/account_view.html', context)
        
    return render(request, 'account/account_view.html', context)    


class SignUpView(View):
    template_name = 'account/sign_up.html'

    def get(self, request):
        # Generate Registration Form
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! Account created. You can now log in.')

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