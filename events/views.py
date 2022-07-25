from django.shortcuts import render, redirect
from .forms import EventsForm
from .models import Events
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def show_events(request):
    context = {'show_events': Events.objects.all()}
    return render(request, "event.html", context)

def event_detail(request, id):
    context = {'event_detail': Events.objects.filter(pk=id)}
    return render(request, "event_detail.html", context)

@staff_member_required(login_url = '/login/')
def event_list(request):
    context = {'event_list': Events.objects.all()}
    return render(request, "event_list.html", context)

@staff_member_required(login_url = '/login/')
def event_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EventsForm()
        else:
            events = Events.objects.get(pk=id)
            form = EventsForm(instance=events)
        return render(request, "event_form.html", {'form': form})
    else:
        if id == 0:
            form = EventsForm(request.POST)
        else:
            events = Events.objects.get(pk=id)
            form = EventsForm(request.POST, instance=events)
        if form.is_valid():
            form.save()
        return redirect('/events/list')

@staff_member_required(login_url = '/login/')
def event_delete(request, id):
    events = Events.objects.get(pk=id)
    events.delete()
    return redirect('/events/list')