from django.shortcuts import render, redirect

from ListingsApp.forms import ListingForm
from ListingsApp.models import Listing


# Create your views here.

def index(request):
    listings = Listing.objects.all()
    return render(request, 'index.html', {'listings': listings})


def add_listing(request):
    if request.method == 'POST':
        form_data = ListingForm(request.POST, files=request.FILES)
        if form_data.is_valid():
            listing = form_data.save(commit=False)
            listing.image = form_data.cleaned_data['image']
            listing.user = request.user
            listing.save()

            return redirect("/index")
    else:
        form = ListingForm()
        return render(request, "add_listing_form.html", {'form': form})

def listing_details(request, id):
    listing = Listing.objects.filter(id=id).get()
    return render(request, "listing_details.html", context={'listing': listing})
