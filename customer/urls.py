from django.urls import path 
from . import views
from .views import *


urlpatterns = [
    path('', views.customerDashboard, name="customerDashboard" ),
    path('<int:slot_id>/', views.displayFields, name="displayFields"),
    path('<int:slot_id>/<int:room_id>/', views.customerRoomBooking, name='customerRoomBooking'),
    path('user-bookings/', views.getUserBookings, name='userRoomBooking'),
    # path('confirm-payment/<int:booking_id>/', views.confirmPayment, name='confirmPayment'),
    path('user-bookings/<int:booking_id>/', views.deatiledUserBooking, name = 'deatiledUserBooking'),
    # path('delete/' , views.deleteUserBooking , name = 'deleteUserBooking') ,
    path("esewa-request/", EsewaRequestView.as_view(), name="esewarequest"),
    path("esewa-verify/", EsewaVerifyView.as_view(), name="esewaverify"),
    path('khalti-request', KhaltiRequestView.as_view(), name='khaltirequest'),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
]
