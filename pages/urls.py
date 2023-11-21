from django.urls import path
from .views import IndexView, LoginView, SignUpView, SuccessLoginView, LoggedOutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='signup'),
    path('loggedin/', SuccessLoginView.as_view(), name='loggedin'),
    path('loggedout/', LoggedOutView.as_view(), name='loggedout'),
] 