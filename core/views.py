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

@api_view(['POST']) 
def calculate_conversion(request):
    amount_aud = request.data.get('amount', 0)
    target_currency = request.data.get('currency', 'NPR')

    # The 'try' block catches errors before they crash the server
    try:
        rate_obj = ExchangeRate.objects.get(currency_code=target_currency)
    except ExchangeRate.DoesNotExist:
        # If the currency isn't in your Admin panel, we send this message instead of crashing
        return Response({
            "error": f"Currency '{target_currency}' not found in database. Please add it in the Admin panel."
        }, status=404)

    # Use 'service_charge' to match your model
    fee = rate_obj.service_charge 
    
    amount_to_convert = float(amount_aud) - float(fee)
    total_recipient_gets = amount_to_convert * float(rate_obj.rate)

    return Response({
        'you_send': amount_aud,
        'our_fee': fee,
        'rate': rate_obj.rate,
        'recipient_gets': round(total_recipient_gets, 2),
        'currency': rate_obj.currency_code 
    })