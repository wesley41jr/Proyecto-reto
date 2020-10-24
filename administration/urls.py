from django.urls import path
from administration.views import panel, show, create, modify, delete
urlpatterns = [
    path('panel/', panel, name='panel'),
    path('eventos/', show, name='show'),
    path('createEvent/', create, name='create'),
    path('modifyEvent/<id>/', modify, name='modify'),
    path('deleteEvent/<id>/', delete, name='delete'),

]
