from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views



app_name = 'social'
urlpatterns = [
    path('',views.profile,name = 'profile'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm),name='login'),
    path('logout/',views.log_out,name="logout"),
    path('register/',views.register,name = "register"),
    path('user/',views.edit_user,name = "edit_account"),
    path('ticket/',views.create_ticket,name = "ticket"),
    
]