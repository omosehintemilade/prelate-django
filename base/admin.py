from django.contrib import admin
from .models import CoveredCountry, TravelInformation, TravelAssistance, TravelInsurance, PostArrivalService, CustomerService
from .models import TourDeal, TravelBudget, UsersCustomTourRequest, TourDealInterest, NewsletterSubscriber
from .models import RequestChange, CustomerReferralRecord

admin.site.register(CoveredCountry)
admin.site.register(TravelInformation)
admin.site.register(TravelAssistance)
admin.site.register(TravelInsurance)
admin.site.register(TourDeal)
admin.site.register(TravelBudget)
admin.site.register(UsersCustomTourRequest)
admin.site.register(TourDealInterest)
admin.site.register(RequestChange)
admin.site.register(CustomerReferralRecord)
admin.site.register(PostArrivalService)
admin.site.register(CustomerService)
admin.site.register(NewsletterSubscriber)
