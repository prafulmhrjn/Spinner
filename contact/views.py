from django.shortcuts import render

# Create your views here.

def show_contact(request):
    return render(request, 'contact.html')