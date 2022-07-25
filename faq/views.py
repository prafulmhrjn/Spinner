from django.shortcuts import render

# Create your views here.

def show_faq(request):
    return render(request, 'faq.html')