from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer

@api_view(['GET'])
# This view will return the latest exchange rate from database
def get_rate(request):
    # 1. Get the very last rate you entered in the Admin panel
    rate_data = ExchangeRate.objects.last()
    
    # 2. Translate it using the Serializer we just made
    serializer = ExchangeRateSerializer(rate_data)
    
    # 3. Send it back as a Response
    return Response(serializer.data)
