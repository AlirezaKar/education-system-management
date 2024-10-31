from django.urls import path
from .views import api_view, home

urlpatterns = [
    path('', home, name='home'),
    path('api/', api_view, name='api_view'),
]