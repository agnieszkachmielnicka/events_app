from django import forms
from main_app.models import Event

class EventForm(forms.ModelForm):

    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id': 'datetimepicker'}), input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Event
        fields = ('title', 'description', 'date')
