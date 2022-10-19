from django.urls import path,include
from .views import *

urlpatterns = [
    path('customer/',CustomerListCreateApi.as_view()),
]

