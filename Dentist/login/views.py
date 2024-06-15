from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def reg_func(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if username and email and password and confirm_password:
            if ("@" not in username and ";" not in username and "," not in username and "!" not in username and "$" not in username and "#" not in username and "%" not in username and "^" not in username and ":" not in username and "&" not in username and "." not in username and "*" not in username and "(" not in username and ")" not in username and "[" not in username and "]" not in username and "{" not in username and "}" not in username and "_" not in username ):
                if '@' in email:
                    if password == confirm_password:
                        User.objects.create_user(
                            username=username,
                            email=email,
                            password=password
                        )
    return render(request, 'login/reg.html')

def auth_func(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main_page')  
    return render(request, 'login/auth.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main_page') 

