from django.shortcuts import render, redirect
from django.views import generic
from main_app.models import Event
from main_app.forms import EventForm
from django.urls import reverse
from django.http import HttpResponseRedirect


class ListEvent(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('date')

class CreateEvent(generic.CreateView):
    model = Event
    form_class = EventForm
    template_name = 'main_app/create_event.html'

    def get_success_url(self):
        return reverse('main_app:event_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

class EventUpdateView(generic.UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'main_app/create_event.html'

    def get_success_url(self):
        return reverse('main_app:event_list')


def join_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.incoming_participants.add(request.user)
    event.save()
    return redirect('main_app:event_list')

def leave_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.incoming_participants.remove(request.user)
    event.save()
    return redirect('main_app:event_list')
