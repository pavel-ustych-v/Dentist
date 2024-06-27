from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse

def reg_func(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        special_chars = ["@", ";", ",", "!", "$", "#", "%", "^", ":", "&", ".", "*", "(", ")", "[", "]", "{", "}", "_"]

        if not all([username, email, password, confirm_password]):
            return JsonResponse({'error': 'Заповніть усі поля, вас не зареєстровано!'}, status=400)

        if any(char in username for char in special_chars):
            return JsonResponse({'error': 'Спеціальні символи, вас не зареєстровано!'}, status=400)

        if '@' not in email:
            return JsonResponse({'error': 'Введіть коректну пошту, вас не зареєстровано!'}, status=400)

        if password != confirm_password:
            return JsonResponse({'error': 'Паролі не співпадають, вас не зареєстровано!'}, status=400)

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return JsonResponse({'success': 'Вас успішно зареєстровано!'})

    return render(request, 'login/reg.html')

def auth_func(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'success': 'Авторизація успішна!'})
            else:
                return JsonResponse({'error': 'Неправильний логін або пароль!'}, status=400)

    return render(request, 'login/auth.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': 'Ви успішно вийшли з акаунту!'})
    return redirect('main_page')
