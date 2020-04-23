from django.shortcuts import render
from .models import CoveredCountry, TravelInformation, TravelInsurace, TourDeal
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(
        request,
        "index.html"
    )

def travel_help(request):
    if request.method == "GET":
        countries = CoveredCountry.objects.all()
        country_requested = request.GET.get("country")

        if not country_requested:
            return render(
                request,
                "travel-help.html",
                context={
                    "countries": countries
                }
            )
        else:
            if country_requested != "":
                print(country_requested)
                return render(
                    request,
                    "travel-help.html",
                    context={
                        "countries": countries,
                        "main_country": CoveredCountry.objects.get(country_name=country_requested)
                    }
                )
            else:
                return render(
                    request,
                    "travel-help.html",
                    context={
                        "countries": countries
                    }
                )
    elif request.method == "POST" and request.is_ajax:
        form_type = request.POST.get("type")
        if form_type == "travelInfo":
            origin =  request.POST.get("origin")
            destination = request.POST.get("destination")
            name = request.POST.get("name")
            phone_number = request.POST.get("phoneNumber")
            email = request.POST.get("email")
            message = request.POST.get("message")

            # Create Record in Table
            TravelInformation.objects.create(
                country_of_origin=CoveredCountry.objects.get(country_name=origin),
                country_of_destination=CoveredCountry.objects.get(country_name=destination),
                fullname=name,
                phonenumber=phone_number,
                email=email,
                enquiry=message
                )

            return JsonResponse({"status" : "success"}, safe=False)

            
        elif form_type == "travelAssist":
            origin =  request.POST.get("origin")
            destination = request.POST.get("destination")
            name = request.POST.get("name")
            dob = request.POST.get("dob")
            phone_number = request.POST.get("phoneNumber")
            email = request.POST.get("email")
            message = request.POST.get("message")
            document = request.FILES

            print(origin, destination, name, dob, phone_number, email, message, document)




def travel_insurance(request):
    if request.method == "GET":
        countries = CoveredCountry.objects.all()
        return render(
            request,
            "travel-insurance.html",
            context={
                "countries": countries,
            }
        )

    if request.method == "POST":
        origin =  request.POST.get("origin")
        destination = request.POST.get("destination")
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        phone_number = request.POST.get("phoneNumber")
        email = request.POST.get("email")
        address = request.POST.get("address")
        insurance_type = request.POST.get("insuranceType")

        # Create Record in Table
        TravelInsurace.objects.create(
            country_of_origin=CoveredCountry.objects.get(country_name=origin),
            country_of_destination=CoveredCountry.objects.get(country_name=destination),
            fullname=name,
            dob=dob,
            phonenumber=phone_number,
            email=email,
            insurance_type=insurance_type,
            address=address
        )

        return JsonResponse({"status" : "success"}, safe=False)





def visa_assistance(request):
    if request.method == "GET":
        countries = CoveredCountry.objects.all()
        country_requested = request.GET.get("country")

        if not country_requested:
            return render(
                request,
                "visa-assistance.html",
                context={
                    "countries": countries
                }
            )
        else:
            if country_requested != "":
                return render(
                    request,
                    "visa-assistance.html",
                    context={
                        "countries": countries,
                        "main_country": CoveredCountry.objects.get(country_name=country_requested)
                    }
                )
            else:
                return render(
                    request,
                    "visa-assistance.html",
                    context={
                        "countries": countries
                    }
                )

def tour(request):
    return render(
        request,
        "tour.html",
        context= {
            "deals": TourDeal.objects.all()

        }
    )

def tour_deal(request, pk, slug):
    package = TourDeal.objects.filter(id=pk, slug=slug).first()
    return render(
        request,
        "tour-deal.html",
        context={
            "package": package
        }
    )

def customize_tour(request):
    return render(
        request,
        "tour-package-customize.html"
    )

def business_travel(request):
    return render(
        request,
        "business-travel.html"
    )

def become_affiliate(request):
    return render(
        request,
        "become-affiliate.html"
    )

def contact_us(request):
    return render(
        request,
        "contact-us.html"
    )

def faq(request):
    return render(
        request,
        "faq.html"
    )