from django.contrib import admin
from .models import CoveredCountry, TravelInformation, TravelAssistance, TravelInsurace
from .models import TourDeal, TravelBudget, UsersCustomTourRequest, TourDealInterest

admin.site.register(CoveredCountry)
admin.site.register(TravelInformation)
admin.site.register(TravelAssistance)
admin.site.register(TravelInsurace)
admin.site.register(TourDeal)
admin.site.register(TravelBudget)
admin.site.register(UsersCustomTourRequest)
admin.site.register(TourDealInterest)
