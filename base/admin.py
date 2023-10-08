from django.contrib import admin
from .models import CoveredCountry, TravelInformation, TravelAssistance, TravelInsurance, PostArrivalService, CustomerService
from .models import TourDeal, TravelBudget, UsersCustomTourRequest, TourDealInterest, NewsletterSubscriber
from .models import RequestChange, CustomerReferralRecord, Consultation, VisaAssistance, Education
from .models import ApplicationInformation, Relationship

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
admin.site.register(Consultation)

# VISA ASSISTANCE


class EducationInline(admin.TabularInline):
    model = Education
    extra = 0


class ApplicationInformationInline(admin.TabularInline):
    model = ApplicationInformation
    extra = 0


class RelationshipInline(admin.TabularInline):
    model = Relationship
    # fieldsets = [
    #     ('Personal Information', {'fields': ['name', 'date_of_birth', 'passport_number']}),
    #     ('Contact Information', {'fields': ['email', 'phone_number']}),
    #     ('Visa Details', {'fields': ['visa_type', 'visa_expiry_date']}),
    # ]
    extra = 0


class VisaAssistanceAdmin(admin.ModelAdmin):
    inlines = [EducationInline,
               ApplicationInformationInline, RelationshipInline]


admin.site.register(VisaAssistance, VisaAssistanceAdmin)
