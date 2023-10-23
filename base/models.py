from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.urls import reverse


TICKET_TYPE = (
    ("ONE WAY", "ONE WAY"),
    ("RETURN TICKET", "RETURN TICKET")
)

TICKET_CLASS = (
    ("FIRST CLASS", "FIRST CLASS"),
    ("BUSINESS", "BUSINESS"),
    ("ECONOMY", "ECONOMY")
)

AIRPORT_PICKUP = (
    ("YES", "YES"),
    ("NO", "NO")
)

HOTEL_RESERVATION = (
    ("YES", "YES"),
    ("NO", "NO")
)

CURRENCY = (
    ("USD", "USD"),
    ("NGN", "NGN")
)

VISA_TYPE = (
    ("STUDENT VISA", "Student Visa"),
    ("WORK VISA", "Work Visa"),
    ("TOURIST VISA", "Tourist Visa"),
    ("BUSINESS VISA", "Business Visa")
)

ACCOMODATION_TYPE = (
    ("SHARED", "Shared Apartment"),
    ("STUDIO", "Studio Apartment"),
    ("2 BEDROOM", "2 Bedroom Apartment")
)

TOUR_CATEGORY = (
    ("INDIVIDUAL", "INDIVIDUAL"),
    ("COUPLE", "COUPLE"),
    ("FAMILY", "FAMILY"),
    ("CORPORATE", "CORPORATE")
)

MEETING_TYPE = (
    ("PHYSICAL", "PHYSICAL"),
    ("VIRTUAL", "VIRTUAL")
)
# Create your models here.


class CoveredCountry(models.Model):
    class Meta:
        verbose_name = "Covered Country"
        verbose_name_plural = "Covered Countries"
        ordering = ["country_name"]

    country_name = models.CharField(max_length=100)
    image_url = models.ImageField(
        blank=True, upload_to="countries/")
    capital_city = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=100, blank=True)
    temperature = models.CharField(max_length=100, blank=True)
    information = RichTextField(blank=True)

    def __str__(self):
        return str(self.country_name)


class NewsletterSubscriber(models.Model):
    class Meta:
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"

    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class TravelInformation(models.Model):
    class Meta:
        verbose_name = "Travel Information"
        verbose_name_plural = "Travel Informations"

    country_of_origin = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="origin")
    country_of_destination = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="destination")
    fullname = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    enquiry = models.TextField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class CustomerService(models.Model):
    class Meta:
        verbose_name = "Customer Service"
        verbose_name_plural = "Customer Services"

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    enquiry = models.TextField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class Consultation(models.Model):
    class Meta:
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"

    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=100)
    session_date = models.DateField()
    session_time = models.TimeField()
    meeting_type = models.CharField(max_length=100, choices=MEETING_TYPE)
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class TravelAssistance(models.Model):
    class Meta:
        verbose_name = "Travel Assistance"
        verbose_name_plural = "Travel Assistance"

    country_of_origin = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="travel_assistance_origin")
    country_of_destination = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="travel_assistance_destination")
    fullname = models.CharField(max_length=200)
    dob = models.DateField()
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    enquiry = models.TextField()
    document = models.ImageField(
        upload_to="travels/", null=True, blank=True)
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class PostArrivalService(models.Model):
    class Meta:
        verbose_name = "Post Arrival Service"
        verbose_name_plural = "Post Arrival Services"

    fullname = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    approved_visa_type = models.CharField(max_length=200, choices=VISA_TYPE)
    document = models.ImageField(
        upload_to="static/uploads/post-arrival-services", null=True, blank=True)
    arrival_date = models.DateField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)
    final_destination = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="post_arrival_services_destination")
    accomodation_type = models.CharField(
        max_length=200, choices=ACCOMODATION_TYPE)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class TravelBudget(models.Model):
    class Meta:
        verbose_name = "Travel Budget"
        verbose_name_plural = "Travel Budgets"

    country_of_origin = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="travel_budget_origin")
    country_of_destination = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="travel_budget_destination")
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPE)
    ticket_class = models.CharField(max_length=20, choices=TICKET_CLASS)
    no_of_travellers = models.CharField(max_length=20)
    airport_pickup = models.CharField(max_length=5, choices=AIRPORT_PICKUP)
    hotel_reservation = models.CharField(
        max_length=5, choices=HOTEL_RESERVATION)
    duration_of_stay = models.CharField(max_length=20)
    estimated_budget_value = models.CharField(max_length=20)
    estimated_budget_currency = models.CharField(
        max_length=3, choices=CURRENCY)
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class TravelInsurance(models.Model):
    class Meta:
        verbose_name = "Travel Insurance"
        verbose_name_plural = "Travel Insurance"

    country_of_origin = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="travel_insurance_origin")
    country_of_destination = models.ForeignKey(
        CoveredCountry, on_delete=models.PROTECT, related_name="travel_insurance_destination")
    fullname = models.CharField(max_length=200)
    dob = models.DateField()
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    insurance_type = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_of_arrival = models.DateField()
    date_of_departure = models.DateField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class TourDeal(models.Model):
    deal_name = models.CharField(max_length=200)
    country = models.CharField(max_length=50,  null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY, null=True)
    amount = models.IntegerField(null=True)
    deal_image = models.ImageField(upload_to="tours/")
    slug = AutoSlugField(populate_from="deal_name")
    information = RichTextField(blank=True)

    def __str__(self):
        return self.deal_name

    def get_absolute_url(self):
        print(self)
        return reverse('tour-deal', args=[self.id, self.slug])


class TourDealInterest(models.Model):
    deal = models.OneToOneField(TourDeal, on_delete=models.PROTECT)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    number_of_travellers = models.IntegerField()

    def __str__(self):
        return "{} requests {}".format(self.fullname, self.deal)


class UsersCustomTourRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=100)
    budget = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    country_of_destination = models.CharField(max_length=100)
    tour_category = models.CharField(max_length=50, choices=TOUR_CATEGORY)
    message = models.TextField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class RequestChange(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=100)
    request_info = models.TextField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class CustomerReferralRecord(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    affiliate_id = models.CharField(max_length=100)
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(self.fullname, self.affiliate_id)
