
from django.urls import path
from .views import SpeedTest

urlpatterns = [
    path('speedtest', SpeedTest.as_view(), name='SpeedTest'),

]
