from django.urls import path
from .views import RegisterView, LoginView, UserView, LogOut

urlpatterns = [
    path('Register', RegisterView.as_view()),
    path('Login', LoginView.as_view()), 
    path('User', UserView.as_view()),
    path('logout', LogOut.as_view()),


]
