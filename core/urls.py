from django.urls import path
from .views import get_rate, calculate_conversion

urlpatterns = [
    # This means: when someone goes to /api/current-rate/, run the get_rate function
    path('current-rate/', get_rate, name='current-rate'),
    path('calculate/', calculate_conversion, name='calculate'), # New line
]