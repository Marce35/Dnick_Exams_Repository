from django import forms
from EventsApp.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user', ]
        widgets = {
            'date_time': forms.DateInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"
            # if not isinstance(field.field.widget, forms.CheckboxInput):
            if visible.name == "isOpenAirEvent":
                visible.field.widget.attrs["class"] = "form-check-input"
