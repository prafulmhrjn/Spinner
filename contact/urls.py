from django.urls import path
from contact import views

urlpatterns = [
    path('',  views.show_contact, name='show_contact'),

]