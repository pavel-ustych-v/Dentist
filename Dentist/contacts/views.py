from django.shortcuts import render

# Create your views here.
def contacts_func(request):
    return render(request, 'contacts/contacts.html')