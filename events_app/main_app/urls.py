from django.conf.urls import url
from main_app import views

app_name = 'main_app'

urlpatterns = [
    url(r'^$', views.ListEvent.as_view(), name='event_list'),
    url(r'^create/$', views.CreateEvent.as_view(), name='create_event'),
    url(r'^join/(?P<event_id>\d+)$', views.join_event, name='join_event'),
    url(r'^leave/(?P<event_id>\d+)$', views.leave_event, name='leave_event'),
    url(r'^edit/(?P<pk>\d+)$', views.EventUpdateView.as_view(), name='edit_event')
]
