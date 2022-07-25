from django.contrib import admin
from .models import DateAndSlot , AvailableRooms , Field
# Register your models here.



allModels = [

    DateAndSlot ,
    AvailableRooms ,
    Field

]


admin.site.register(allModels)
