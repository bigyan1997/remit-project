from django.contrib import admin
from .models import User, ExchangeRate

# This makes your custom User (email-based) show up in Admin
admin.site.register(User)

# This makes the ExchangeRate calculator settings show up in Admin
admin.site.register(ExchangeRate)