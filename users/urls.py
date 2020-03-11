from django.urls import path, include
from .views import *

app_name = 'users'


urlpatterns = [
    path('registration/', UserCreate.as_view(), name='user_create_url'),
    path('login/', UserLogin.as_view(), name='login'),
]
