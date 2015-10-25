from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^me/allot$', views.seatAlloc, name='allot_seats'),
]
