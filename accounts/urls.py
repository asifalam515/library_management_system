
from django.urls import path
from .views import UserLoginView,UserRegistrationView,user_logout,update_profile,change_password

urlpatterns = [
    
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', user_logout,name='logout'),
    path('profile/', update_profile,name='profile'),
    path('change_password/', change_password,name='change_password'),
]
