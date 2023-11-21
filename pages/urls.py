from django.urls import path
from .views import IndexView, LoginView, SignUp

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignUp.as_view(), name='signup')
] 