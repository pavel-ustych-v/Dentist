from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.
def price_func(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        if request.POST.get('search'):
            categories = categories.filter(name__icontains = request.POST.get('search'))    
    return render(request, 'price/price.html', context = {'categories': categories,'services': Service.objects.all()})