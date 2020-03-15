from django.contrib.auth.forms import PasswordChangeForm,\
    UserCreationForm, UserChangeForm,PasswordResetForm, SetPasswordForm
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label=('Пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label=('Повторите пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta(UserCreationForm):
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email'
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
                ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        rs = CustomUser.objects.filter(email=email)
        if rs.count():
            raise ValidationError("Такой email уже существует!")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают!")
        return password2

class LoginForm(forms.Form):
    email = forms.EmailField(
        label=('Email'),
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    password = forms.CharField(
        label=('Пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta(object):
        model = CustomUser

        fields = [
            'email', 'password'
        ]

class PassChForm(PasswordChangeForm):
    error_messages = {
        'password_mismatch': "Пароли не совпадают",
        'password_incorrect': "Неверный старый пароль. "
                                "Попробуйте еще раз.",
    }

    old_password = forms.CharField(
        label=('Старый пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label=('Новый пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label=('Повторите пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

# Наследуемся от стандартного сброса пароля и делаем свое поле для mail
class PassResForm(PasswordResetForm):
    email = forms.EmailField(
        label=('Email'),
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )


class SetPassForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': "Пароли не совпадают",
    }
    new_password1 = forms.CharField(
        label=('Новый пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label=('Повторите пароль'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('user_image', 'email', 'first_name', 'last_name',)
