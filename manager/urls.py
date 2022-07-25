from . import views 
from django.urls import path 


urlpatterns = [
    path('managerdashboard' , views.managerDashboard , name = 'managerDashboard' ) ,
    path('addfield' , views.addRooms , name = 'addFields') ,
    path('addfield/<int:slot_id>' , views.addRooms_2 , name = 'addFields') ,
    path('addslot' , views.addSlot , name = 'addSlot' ) ,
    path('getAllBookedDates' , views.getAllBookedDates , name = 'getAllBookedDates' ) ,
    path('getAllBookedDates/<int:slot_id>' , views.getSlotBookingDetail , name = 'getSlotBookingDetail' ) ,
    path('getAllBookedDates/userBookingDetails/<int:booking_id>' , views.userBookingDetail , name = 'userBookingDetail' ) ,
]
