
from django.contrib import admin
from django.urls import path , include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('registration.urls')) , 
    path('' , include('manager.urls')) , 
    path('customer/' , include('customer.urls')) ,
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('faq/', include('faq.urls')),
    path('news/', include('news.urls')),
    path('events/', include('events.urls')),
]
