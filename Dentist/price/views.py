from django.shortcuts import render
from .models import *
# Create your views here.
def price_func(request):
    context = {'categories': Category.objects.all()}

    context['services'] = Service.objects.all()
    return render(request, 'price/price.html', context)