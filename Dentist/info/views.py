from django.shortcuts import render

# Create your views here.
def info_func(request):
    return render(request, 'info/info.html')