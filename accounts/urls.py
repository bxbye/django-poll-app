from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

app_name = "accounts"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', login_required(views.profile), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]