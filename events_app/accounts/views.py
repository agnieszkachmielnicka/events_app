from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm


def custom_login_view(request):

    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = email.split('@')[0]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main_app:event_list')

    return render(request, 'accounts/login.html', {'form': form})


def registration_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('email').split('@')[0]
        user.set_password(password)
        user.username = username
        user.save()
        return redirect('accounts:login')

    return render(request, 'accounts/register.html', {'form': form})
