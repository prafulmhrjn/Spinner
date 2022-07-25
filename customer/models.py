from django.db import models
from manager.models import AvailableRooms , DateAndSlot , Field

METHOD = (
    ('Cash', 'Cash'),
    ('Khalti', 'Khalti'),
    ('Esewa', 'Esewa')
)

class RoomBooking(models.Model):
    booking_date_slot = models.ForeignKey(DateAndSlot , on_delete=models.CASCADE , blank=False)
    booked_room_number = models.OneToOneField(Field , unique = True , on_delete = models.CASCADE , blank = False, related_name='+')
    bookee_username = models.CharField(max_length = 50 , blank = False , default = 'Admin')
    # booking_price = modatedels.OneToOneField(Room, on_delete = models.CASCADE, blank=False)
    # date_price = models.ForeignKey(DateAndSlot, on_delete = models.CASCADE, related_name='+', default=4500)
    payment_method = models.CharField(max_length=20, choices=METHOD, default="Cash")
    payment_completed = models.BooleanField(default=False, null=True, blank=True)


    #field to be taken as input
    customer_name = models.CharField(max_length = 60 , blank=False)
    customer_email = models.EmailField(unique = True, max_length=254)
    customer_contact = models.CharField(unique = True , max_length = 12)
    booking_purpose = models.CharField(max_length = 254 , blank = True)

    def __str__(self):
        return self.customer_name 
