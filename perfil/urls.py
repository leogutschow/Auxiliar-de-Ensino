from django.urls import path, include
from .views import Dashboard, LogOut, SignIn, LogIn

urlpatterns = [
    path('login', LogIn.as_view(),name='login'),
    path('logout', LogOut.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('signin', SignIn.as_view(), name='signin'),
    
]
