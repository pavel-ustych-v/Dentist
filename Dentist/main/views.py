from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def main_func(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        send_mail( 
            'Проблема',
            f"Ім'я клієнта: {name} \nПроблема: {problem}",
            settings.EMAIL_HOST_USER,
            [email]
            )
    return render(request, 'main/main.html')
