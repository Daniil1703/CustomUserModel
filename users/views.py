from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractBaseUser
from .models import CustomUser
from .forms import CustomUserCreationForm, LoginForm


class UserCreate(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(
            request, 'users/registration.html', context={'form': form}
        )

    def post(self, request):
        if request.method == 'POST':
            bound_form = CustomUserCreationForm(request.POST)
            if bound_form.is_valid():
                bound_form.save()
                messages.success(request, 'Аккаунт успешно создан!')
                return redirect('mainsite:dashboard')
        else:
            bound_form = CustomUserCreationForm()
        return render(
               request, 'users/registration.html', context={'form': bound_form}
               )

class UserLogin(View):

    def get(self, request):
        form = LoginForm()
        return render(
            request, 'users/login.html', context={'form': form}
        )

    def post(self, request):
        if request.method == 'POST':
            bound_form = LoginForm(request.POST)
            if bound_form.is_valid():
                cd = bound_form.cleaned_data
                user = authenticate(
                    request, email=cd['email'], password=cd['password']
                )
            if user is not None:
                if user.is_active:
                    login(request,user)
                    messages.success(request, 'Вы успешно вошли в систему!')
                    return redirect('mainsite:dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                messages.error(
                    request, 'Неверный адрес электронной почты или пароль'
                    )
                return redirect('users:login')
        else:
            bound_form = LoginForm()
        return render(
               request, 'users/login.html', context={'form': bound_form}
               )

def message_change_password(request):
    messages.success(request, 'Вы успешно сменили пароль!')
    return redirect('mainsite:dashboard')

def logout_view(request):
    logout(request)
    messages.warning(request, 'Вы вышли из системы!')
    return redirect('users:login')
