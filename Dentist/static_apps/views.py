from django.shortcuts import render

# Create your views here.
def contacts_func(request):
    return render(request, 'static_apps/contacts.html')

def info_func(request):
    return render(request, 'static_apps/info.html')

def services_func(request):
    return render(request, 'static_apps/services.html')