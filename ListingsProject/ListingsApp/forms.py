from django import forms
from ListingsApp.models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['user', ]
        widgets = {
            'datetime': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'isNewListing':
                visible.field.widget.attrs['class'] = 'form-check-input'
