from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.custom_login_view, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.registration_view, name='register')
]
