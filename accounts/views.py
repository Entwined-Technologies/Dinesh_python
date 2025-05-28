from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm, RegisterForm

def login_view(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                return render(request, 'accounts/profile.html', {'username': username})
            except User.DoesNotExist:
                message = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'message': message})

def register_view(request):
    message = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                message = 'Passwords do not match'
            elif User.objects.filter(username=username).exists():
                message = 'Username already exists'
            else:
                User.objects.create(username=username, password=password)
                return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form, 'message': message})

def logout_view(request):
    # Since we are not using Django's auth system, just redirect to login page
    return redirect('login')
