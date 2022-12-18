from django.urls import path
from .views import *

app_name = 'services'

urlpatterns = [
    path('services/', ServicesList.as_view(), name='services'),
    path('service/<int:pk>/', ServicesDetail.as_view(), name='service'),
]