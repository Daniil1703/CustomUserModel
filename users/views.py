from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CustomUserCreationForm


class UserCreate(View):
    """docstring for UserCreate."""

    def get(self, request):
        form = CustomUserCreationForm()
        return render(
            request,
            'users/registration.html',
            context={'form': form})

    def post(self, request):
        if request.method == 'POST':
            bound_form = CustomUserCreationForm(request.POST)
            if bound_form.is_valid():
                bound_form.save()
                messages.success(request, 'Аккаунт успешно создан!')
                return redirect('mainsite:dashboard')
        else:
            bound_form = CustomUserCreationForm()
        return render(request, 'users/registration.html',context={'form': bound_form})
