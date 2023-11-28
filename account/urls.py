from django.urls import path
from .views import LoginView, SignUpView, SuccessLoginView, LoggedOutView, AccountDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('loggedin/', SuccessLoginView.as_view(), name='loggedin'),
    path('loggedout/', LoggedOutView.as_view(), name='loggedout'),
    path('account/<str:username>/', AccountDetailView.as_view(), name='accountview'),
] 