from django.urls import path
from . import views

urlpatterns = [
    path('',  views.show_events, name='show_events'),
    path('<int:id>',  views.event_detail, name='event_detail'),
    path('insert',  views.event_form, name='event_insert'),
    path('update/<int:id>',  views.event_form, name='event_update'),
    path('delete/<int:id>',  views.event_delete, name='event_delete'),
    path('list',  views.event_list, name='event_list')

]