from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import SignUpForm, LoginForm
from .models import AccountAvatar

class ProfileView(View):
    pass

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        
        return render(request, 'account/signup.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            #Create Profile with Defaulted Icon
            AccountAvatar.objects.create(user=user)
            return redirect('login')
        
        else:
            return render(request, 'account/signup.html', {'form': form})
        
class LoginView(View):
    def get(self, request):
        form = LoginForm()

        if request.user.is_authenticated:
            return redirect('index')
        
        else:
            return render(request, 'account/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            # Authenticate Username/Password Inputted
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('loggedin')
            
            else:
                return render(request, 'account/login.html', {'form': form, 'error_message' : 'Did not find a match with username/password combination'})
            
        else:
            return render(request, 'account/login.html', {'form': form})
    
class SuccessLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'account/loggedin.html')
        
        else:
            return redirect('login')
    
class LoggedOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        
        else:
            redirect('login')
            
        return render(request, 'account/loggedout.html')