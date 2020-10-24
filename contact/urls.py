from django.urls import path
from contact import views


urlpatterns = [
    path('message', views.contact, name='contact'),
]
