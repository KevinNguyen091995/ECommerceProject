from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import VerifiedUser, AccountAvatar

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    #Create and save avatar and verified user
    def save(self, commit=True):
        user = super().save(commit)
        account_avatar = AccountAvatar.objects.create(user = user)
        verified_user = VerifiedUser.objects.create(user = user)

        return account_avatar, verified_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Enter Username','autocomplete': 'off'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','autocomplete': 'off','data-toggle': 'password'}))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'