from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class CoveredCountry(models.Model):
    class Meta:
        verbose_name = "Covered Country"
        verbose_name_plural = "Covered Countries"

    country_name = models.CharField(max_length=100)
    image_url = models.ImageField(blank=True, upload_to="static/uploads/countries")
    capital_city = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=100, blank=True)
    temperature = models.CharField(max_length=100, blank=True)
    information = RichTextField(blank=True)

    def __str__(self):
        return str(self.country_name)



class TravelInformation(models.Model):
    class Meta:
        verbose_name = "Travel Information"
        verbose_name_plural = "Travel Information"

    country_of_origin = models.ForeignKey(CoveredCountry, on_delete=models.PROTECT, related_name="origin")
    country_of_destination = models.ForeignKey(CoveredCountry, on_delete=models.PROTECT, related_name="destination")
    fullname = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    enquiry = models.TextField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])

    


class TravelAssistance(models.Model):
    class Meta:
        verbose_name = "Travel Assistance"
        verbose_name_plural = "Travel Assistance"

    country_of_origin = models.ForeignKey(CoveredCountry, on_delete=models.PROTECT, related_name="travel_assistance_origin")
    country_of_destination = models.ForeignKey(CoveredCountry, on_delete=models.PROTECT, related_name="travel_assistance_destination")
    fullname = models.CharField(max_length=200)
    dob = models.DateField()
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    enquiry = models.TextField()
    document = models.ImageField(upload_to="static/uploads/travels")
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])


class TravelInsurace(models.Model):
    class Meta:
        verbose_name = "Travel Insurance"
        verbose_name_plural = "Travel Insurance"

    country_of_origin = models.ForeignKey(CoveredCountry, on_delete=models.PROTECT, related_name="travel_insurance_origin")
    country_of_destination = models.ForeignKey(CoveredCountry, on_delete=models.PROTECT, related_name="travel_insurance_destination")
    fullname = models.CharField(max_length=200)
    dob = models.DateField()
    phonenumber = models.CharField(max_length=100)
    email = models.EmailField()
    insurance_type = models.CharField(max_length=200)
    address = models.TextField()
    datetime_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} | Time of Record:{}".format(self.email, str(self.datetime_of_entry)[:16])

    
class TourDeal(models.Model):
    deal_name = models.CharField(max_length=200)
    deal_image = models.ImageField(upload_to="static/uploads/tours")
    slug = AutoSlugField(populate_from="deal_name")
    information = RichTextField(blank=True)
    
    def __str__(self):
        return self.deal_name

    def get_absolute_url(self):
        return reverse('tour-deal', args=[self.id, self.slug])