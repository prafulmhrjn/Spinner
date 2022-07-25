from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='news_main'),
    path('<int:id>', views.news_detail, name='news_detail'),
    path('insert', views.news_form, name='news_insert'),
    path('update/<int:id>', views.news_form, name='news_update'),
    path('delete/<int:id>', views.news_delete, name='news_delete'),
    path('list', views.news_list, name='news_list')
]