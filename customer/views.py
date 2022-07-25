#Importing django utils
import requests as requests
from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.http import HttpResponse , Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views import View

#Import Model and Forms
from .forms import RoomBookingForm
from manager.models import DateAndSlot , Field , AvailableRooms
from .models import RoomBooking
from django.http import JsonResponse


#import system datetime
import datetime


#Customer Dashboard
def customerDashboard(request):
    if request.user.is_authenticated:
        room_list = Field.objects.filter(is_booked = False) # all unbooked room objects

        date_slot_list = []
        for room in room_list:
            if room.chosen_date_slot not in date_slot_list:
                date_slot_list.append(room.chosen_date_slot)

        all_date_slot_list = DateAndSlot.objects.all().order_by('booking_date')

        full_slots = list(set(all_date_slot_list) - set(date_slot_list))

        # getting full slots and available slots

        content = {
                'full_slots'     : full_slots ,
                'date_slot_list' : date_slot_list ,
            }
        return render(request, "customer/customerDashboard.html",content)
    else:
        return render(request, "sorry_page.html")


# display the rooms available for particular slot
@login_required(login_url='/login/')
def displayFields(request, slot_id):

    selected_slot_obj = DateAndSlot.objects.get(pk = slot_id)
    room_list_for_slot = Field.objects.filter(chosen_date_slot = selected_slot_obj , is_booked = False) # Display unbooked rooms for the selected slot

    content = {
        'room_list_for_slot': room_list_for_slot
    }
    return render(request , "customer/displayFields.html" , content)


# For displaying all the user bookings
@login_required(login_url='/login/')
def getUserBookings(request):

    user_booking_list = RoomBooking.objects.filter(bookee_username = request.user) # User Bookings
    current_date = datetime.date.today()


    content = {
            'user_booking_list' : user_booking_list ,
            'today'             : current_date ,

        }


    return render(request , 'customer/userBookings.html' , content)


@login_required(login_url='/login/')
def customerRoomBooking(request, slot_id , room_id):
    # Handle POST request
    if request.POST :
        rb = RoomBooking()
        rb.booked_room_number = Field.objects.get(pk = room_id)
        rb.bookee_username = request.user.username
        rb.booking_date_slot = DateAndSlot.objects.get(pk = slot_id )

        form = RoomBookingForm(request.POST, instance = rb)
        if form.is_valid():
            pm = form.cleaned_data.get("payment_method")
            room = Field.objects.get(pk = room_id)
            booking = form.save()
            room.is_booked = True
            room.save()
            booking.save()
            if pm == "Khalti":
                return redirect(reverse('khaltirequest') + "?o_id=" + str(booking.id) + "&amt=" + str(DateAndSlot.objects.get(pk = slot_id ).booking_price))
            elif pm == "Esewa":
                return redirect(reverse('esewarequest') + "?o_id=" + str(booking.id) + "&amt=" + str(DateAndSlot.objects.get(pk = slot_id ).booking_price))
            return redirect(reverse('userRoomBooking'))

    # Handle GET request
    form = RoomBookingForm()
    room_number = Field.objects.get(pk = room_id).room_number
    booking_price = DateAndSlot.objects.get(pk = slot_id).booking_price
    content = {
        'room_number': room_number,
        'booking_price': booking_price,
        'form': form
    }
    return render(request, "customer/customerRoomBooking.html", content)

class KhaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        booking_id = request.GET.get("o_id")
        order = RoomBooking.objects.get(pk=booking_id)
        # Field.objects.get(pk=room_id)
        context = {
            "order": order,
            "amt": 20


        }
        return render(request, "customer/khaltirequest.html", context)


class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        o_id = request.GET.get("booking_id")
        print(token, amount, o_id)

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": "Key test_secret_key_f59e8b7d18b4499ca40f68195a846e9b"
        }

        order_obj = RoomBooking.objects.get(id=o_id)

        response = requests.post(url, payload, headers=headers)
        resp_dict = response.json()
        if resp_dict.get("idx"):
            success = True
            order_obj.payment_completed = True
            order_obj.save()
        else:
            success = False
        data = {
            "success": success
        }
        return JsonResponse(data)


class EsewaRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = RoomBooking.objects.get(id=o_id)
        context = {
            "order": order,
            "amt": request.GET.get("amt")
        }
        return render(request, "customer/esewarequest.html", context)


class EsewaVerifyView(View):
    def get(self, request, *args, **kwargs):
        import xml.etree.ElementTree as ET
        oid = request.GET.get("oid")
        amt = request.GET.get("amt")
        refId = request.GET.get("refId")

        url = "https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amt,
            'scd': 'epay_payment',
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)
        root = ET.fromstring(resp.content)
        status = root[0].text.strip()

        booking_id = oid.split("_")[1]
        order_obj = RoomBooking.objects.get(id=booking_id)
        if status == "Success":
            order_obj.payment_completed = True
            order_obj.save()
            # return redirect('customer/show_thank')
            return render(request, "customer/thankYouPage.html")
        else:

            return redirect("/esewa-request/?o_id="+booking_id)


# Get the details of user bookings .
def deatiledUserBooking(request, booking_id):
    user_booking_detail = get_object_or_404(RoomBooking, pk=booking_id)

    if request.method == 'POST':
        user_booking_detail.booked_room_number.is_booked = False
        user_booking_detail.booked_room_number.save()
        user_booking_detail.delete()
        messages.success(request, 'Booking Cancelled Successfully!!')
        return redirect(reverse('userRoomBooking'))

    content = {
        'booking': user_booking_detail,
    }
    return render(request, 'customer/detailedUserBooking.html', content)



