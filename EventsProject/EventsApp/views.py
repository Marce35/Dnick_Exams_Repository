from datetime import datetime

from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from EventsApp.forms import EventForm
from EventsApp.models import Event, Band, BandEvent


# Create your views here.

def index(request):
    events = Event.objects.annotate(num_bands=Count('bandevent'))
    return render(request, 'index.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form_data = EventForm(request.POST, files=request.FILES)
        if form_data.is_valid():
            event = form_data.save(commit=False)
            event.image = form_data.cleaned_data['image']
            event.user = request.user
            event.save()
            bands = form_data.cleaned_data['bands']
            event.bands = bands
            band_list = [band.strip() for band in bands.split(',') if band.strip()]
            print("Band List:", band_list)
            for band in band_list:
                band_obj = Band.objects.filter(name=band).first()
                if band_obj:
                    band_obj.number_of_events = band_obj.number_of_events + 1
                    band_obj.save()
                    BandEvent.objects.create(band=band_obj, event=event)
            return redirect("/index")
    else:
        form = EventForm()
        return render(request, "add_event_form.html", {'form': form})


def edit_event(request, id):
    event_instance = Event.objects.filter(id=id).get()
    if request.method == 'POST':
        event = EventForm(request.POST, instance=event_instance)
        if event.is_valid():
            event.save()
        return redirect("/index")
    else:
        event = EventForm(instance=event_instance)
        return render(request, "edit_event_form.html", {'form': event})


# def delete_event(request, id):
#     event_instance = Event.objects.filter(id=id).get()
#     if request.method == 'POST':
#         event_instance.delete()
#         return redirect("/index")
#     else:
#         return render(request, "delete_event_form.html")

def delete_event(request, id):
    event_instance = get_object_or_404(Event, id=id)
    if event_instance:
        event_instance.delete()
    return redirect("/index")

