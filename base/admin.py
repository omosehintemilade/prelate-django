from django.contrib import admin
from .models import CoveredCountry, TravelInformation, TravelAssistance, TravelInsurace, PostArrivalService, CustomerService
from .models import TourDeal, TravelBudget, UsersCustomTourRequest, TourDealInterest
from .models import RequestChange, CustomerReferralRecord

admin.site.register(CoveredCountry)
admin.site.register(TravelInformation)
admin.site.register(TravelAssistance)
admin.site.register(TravelInsurace)
admin.site.register(TourDeal)
admin.site.register(TravelBudget)
admin.site.register(UsersCustomTourRequest)
admin.site.register(TourDealInterest)
admin.site.register(RequestChange)
admin.site.register(CustomerReferralRecord)
admin.site.register(PostArrivalService)
admin.site.register(CustomerService)
