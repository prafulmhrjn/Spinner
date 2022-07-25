from django import forms
from .models import Events

class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = ('event_title', 'event_description', 'event_snippet', 'event_date_time', 'event_location')
        labels = {
            'event_title': 'Event Title (Enter the event title please)',
            'event_description': 'Event Description (Enter the event description please)',
            'event_snippets': 'Event Snippets (Enter the event snippets please)',
            'event_date_time': 'Event Date (Enter the event publisher please)',
            'event_location': 'Event Location (Enter the event publisher please)'
        }

