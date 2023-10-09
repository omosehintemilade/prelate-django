import os
import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import CoveredCountry, TravelInformation, TourDeal, TravelAssistance, TravelInsurance
from .models import CustomerReferralRecord, Consultation, VisaAssistance, Education
from .models import ApplicationInformation, Relationship, OtherInformation
from django.http import JsonResponse, HttpResponseRedirect
from acctmang.models import User, Profile, UserTransactionRecord, UserEarnings
from django.contrib.auth.decorators import login_required
from acctmang.forms import EditProfileInformation
import datetime
import calendar
import decimal
from django.db.models import Sum, Q
import requests
from .forms import TravelInformationForm, TravelAssistanceForm, TravelBudgetForm, PostArrivalServiceForm, CustomerServiceForm, ConsultationForm
from .forms import UsersCustomTourRequestForm, TourDealInterestForm, RequestChangeForm, TravelInsuranceForm, NewsletterSubscriberForm, VisaAssistanceForm


def home(request):
    return render(
        request,
        "index.html"
    )
    # return redirect("https://flights.prelatetravel.com/index.php")


def homeOld(request):
    return render(
        request,
        "index-old.html"
    )


def reservations(request):
    return render(
        request,
        "reservations.html"
    )


def travel_helpOld(request):
    if request.method == "GET":
        countries = CoveredCountry.objects.all().order_by("country_name")
        country_requested = request.GET.get("country")

        if not country_requested:
            return render(
                request,
                "travel-help-old.html",
                context={
                    "countries": countries,
                    "travel_info_form": TravelInformationForm(),
                    "travel_assistance_form": TravelAssistanceForm(),
                    "travel_budget_form": TravelBudgetForm(),
                    "request_change_form": RequestChangeForm()
                }
            )
        else:
            if country_requested != "":
                print(country_requested)
                return render(
                    request,
                    "travel-help-old.html",
                    context={
                        "countries": countries,
                        "main_country": CoveredCountry.objects.get(country_name=country_requested),
                        "travel_info_form": TravelInformationForm(),
                        "travel_assistance_form": TravelAssistanceForm(),
                        "travel_budget_form": TravelBudgetForm(),
                        "request_change_form": RequestChangeForm()

                    }
                )
            else:
                return render(
                    request,
                    "travel-help-old.html",
                    context={
                        "countries": countries,
                        "travel_info_form": TravelInformationForm(),
                        "travel_assistance_form": TravelAssistanceForm(),
                        "travel_budget_form": TravelBudgetForm(),
                        "request_change_form": RequestChangeForm()

                    }
                )


def travel_help(request):
    if request.method == "GET":
        countries = CoveredCountry.objects.all().order_by("country_name")
        country_requested = request.GET.get("country")

        if not country_requested:
            return render(
                request,
                "travel-help.html",
                context={
                    "countries": countries,
                    "travel_info_form": TravelInformationForm(),
                    "travel_assistance_form": TravelAssistanceForm(),
                    "travel_budget_form": TravelBudgetForm(),
                    "request_change_form": RequestChangeForm()
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
                        "main_country": CoveredCountry.objects.get(country_name=country_requested),
                        "travel_info_form": TravelInformationForm(),
                        "travel_assistance_form": TravelAssistanceForm(),
                        "travel_budget_form": TravelBudgetForm(),
                        "request_change_form": RequestChangeForm()

                    }
                )
            else:
                return render(
                    request,
                    "travel-help.html",
                    context={
                        "countries": countries,
                        "travel_info_form": TravelInformationForm(),
                        "travel_assistance_form": TravelAssistanceForm(),
                        "travel_budget_form": TravelBudgetForm(),
                        "request_change_form": RequestChangeForm()
                    }
                )


def travel_info(request):
    if request.method == "POST":
        form = TravelInformationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return redirect("/travel-help#submitted")


def subscribe_to_newsletter(request):
    if request.method == "POST":
        form = NewsletterSubscriberForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            redirect_url = request.META.get('HTTP_REFERER', '/')
            return HttpResponseRedirect(redirect_url + "#submitted?action=subscribe")


def travel_assistance(request):
    if request.method == "POST":
        form = TravelAssistanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/travel-help#submitted?redirect=travel-info")


def travel_budget(request):
    if request.method == "POST":
        form = TravelBudgetForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return redirect("/travel-help#submitted?redirect=travel-budget")


def request_change(request):
    if request.method == "POST":
        form = RequestChangeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return redirect("/travel-help#submitted?redirect=request-changes")


def travel_insurance(request):
    if request.method == "GET":
        return render(
            request,
            "travel-insurance.html",
            context={
                "form": TravelInsuranceForm()
            }
        )
    if request.method == "POST":
        form = TravelInsuranceForm(request.POST)
        print("vaild from", form.is_valid())
        if form.is_valid():
            form.save(commit=True)
            print("to redirect.....")
            return redirect("/travel-insurance#submitted")


def travel_insuranceOld(request):
    if request.method == "GET":
        countries = CoveredCountry.objects.all().order_by("country_name")
        return render(
            request,
            "travel-insurance-old.html",
            context={
                "countries": countries,
            }
        )

    if request.method == "POST":
        origin = request.POST.get("origin")
        destination = request.POST.get("destination")
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        phone_number = request.POST.get("phoneNumber")
        email = request.POST.get("email")
        address = request.POST.get("address")
        insurance_type = request.POST.get("insuranceType")

        # Create Record in Table
        TravelInsurance.objects.create(
            country_of_origin=CoveredCountry.objects.get(country_name=origin),
            country_of_destination=CoveredCountry.objects.get(
                country_name=destination),
            fullname=name,
            dob=dob,
            phonenumber=phone_number,
            email=email,
            insurance_type=insurance_type,
            address=address
        )

        return JsonResponse({"status": "success"}, safe=False)


def visa_assistance(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        applicant_info = json_data.get('applicant_info')
        education_history = json_data.get('education_history')
        application_info = json_data.get('application_info')
        relationships = json_data.get('relationships')
        other_info = json_data.get('other_info')

        # Create a visa assistance instance
        applicant = VisaAssistance(**applicant_info)
        # stringify Travel history - in my opinion, it's not worth creating a new table for
        print("applicant_info.travel_history ==>",
              applicant_info.get("travel_history"))
        applicant.set_travel_history_list(
            applicant_info.get("travel_history"))
        applicant.save()

        # Check if education_history is a valid list
        if isinstance(education_history, list):
            # Iterate over the list
            for ed in education_history:
                ed["applicant"] = applicant
                print(ed)
                Education.objects.create(**ed)

        # Application Information
        application_info["applicant"] = applicant
        application_info["country"] = CoveredCountry.objects.get(
            country_name=application_info.get("country"))
        ApplicationInformation.objects.create(**application_info)

        # Create Relationships
        # Check if relationships is a valid list
        if isinstance(relationships, list):
            # Iterate over the list and create relationship
            for relationship in relationships:
                relationship["applicant"] = applicant
                print(relationship)
                Relationship.objects.create(**relationship)

        # Other Information
        other_info_doc = OtherInformation(**other_info)
        other_info_doc.applicant = applicant
        other_info_doc.set_extra_curicular_activities_list(
            other_info.get("extra_curicular_activities"))
        other_info_doc.save()

        return JsonResponse({"status": "success"}, safe=False)
    else:
        countries = CoveredCountry.objects.all().order_by("country_name")
        return render(
            request,
            "visa-assistance.html",
            context={
                "countries": countries,
            }
        )


def visa_assistance_old(request):
    if request.method == "GET":
        countries = CoveredCountry.objects.all().order_by("country_name")
        country_requested = request.GET.get("country")

        if not country_requested:
            return render(
                request,
                "visa-assistance-old.html",
                context={
                    "countries": countries,
                    "travel_assistance_form": TravelAssistanceForm(),
                }
            )
        else:
            if country_requested != "":
                return render(
                    request,
                    "visa-assistance-old.html",
                    context={
                        "countries": countries,
                        "main_country": CoveredCountry.objects.get(country_name=country_requested),
                        "travel_assistance_form": TravelAssistanceForm(),

                    }
                )
            else:
                return render(
                    request,
                    "visa-assistance.html",
                    context={
                        "countries": countries,
                        "travel_assistance_form": TravelAssistanceForm(),

                    }
                )
    elif request.method == "POST":
        countries = CoveredCountry.objects.all().order_by("country_name")
        form = TravelAssistanceForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save(commit=True)
            return redirect("/visa-assistance#submitted")
        else:
            return render(
                request,
                "visa-assistance.html",
                context={
                    "countries": countries,
                    "travel_assistance_form": TravelAssistanceForm(),

                }
            )


def post_arrival_services(request):
    if request.method == "POST":
        form = PostArrivalServiceForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save(commit=True)
            return redirect("/post-arrival-services#submitted")
    else:
        return render(
            request,
            "post-arrival-services.html",
            context={
                "form": PostArrivalServiceForm()
            }
        )


def tour(request):
    return render(
        request,
        "tour.html",
        context={
            "deals": TourDeal.objects.all()
        }
    )


def tourOld(request):
    return render(
        request,
        "tour-old.html",
        context={
            "deals": TourDeal.objects.all()

        }
    )


def tour_deal_old(request, pk, slug):
    package = TourDeal.objects.filter(id=pk, slug=slug).first()

    if request.method == "GET":
        return render(
            request,
            "tour-deal-old.html",
            context={
                "package": package,
                "form": TourDealInterestForm(initial={
                    'deal': package
                })
            }
        )
    elif request.method == "POST":
        form = TourDealInterestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

        redirect_link = "/tour/{}/{}#submitted".format(pk, slug)
        return redirect(redirect_link)


def tour_deal(request, pk, slug):
    package = TourDeal.objects.filter(id=pk, slug=slug).first()

    if request.method == "GET":
        return render(
            request,
            "tour-deal.html",
            context={
                "package": package,
                "form": TourDealInterestForm(initial={
                    'deal': package
                })
            }
        )
    elif request.method == "POST":
        form = TourDealInterestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

        redirect_link = "/tour/{}/{}#submitted".format(pk, slug)
        return redirect(redirect_link)


def customize_tour(request):
    if request.method == "GET":
        return render(
            request,
            "tour-package-customize.html",
            {
                "form": UsersCustomTourRequestForm()
            }
        )
    elif request.method == "POST":
        form = UsersCustomTourRequestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

        return redirect("/tour/customize#submitted")


def customize_tourOld(request):
    if request.method == "GET":
        return render(
            request,
            "tour-package-customize-old.html",
            {
                "form": UsersCustomTourRequestForm()
            }
        )
    elif request.method == "POST":
        form = UsersCustomTourRequestForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

        return redirect("/tour-package-customize#submitted")


def business_travel(request):
    return render(
        request,
        "business-travel.html",
        context={
            "form": TravelInsuranceForm()
        }
    )


def business_travel_old(request):
    return render(
        request,
        "business-travel-old.html"
    )


def become_affiliate(request):
    return render(
        request,
        "become-affiliate.html"
    )


def become_affiliate_old(request):
    return render(
        request,
        "become-affiliate-old.html"
    )


def contact_us(request):
    if request.method == "POST":
        form = CustomerServiceForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/contact-us#submitted")
    else:
        return render(
            request,
            "contact-us.html",
            context={
                "form": CustomerServiceForm()
            }
        )


def contact_us_old(request):
    return render(
        request,
        "contact-us-old.html"
    )


def book_consultation(request):
    if request.method == "POST":
        form = ConsultationForm(request.POST)

        if form.is_valid():
            # VALIDATE DATE
            session_date = form.cleaned_data['session_date']
            session_time = form.cleaned_data['session_time']

            # Check if a session with the same datetime exists
            if Consultation.objects.filter(session_date=session_date, session_time=session_time).exists():
                return redirect("/book-consultation#error?type=duplicate_event")
            else:
                form.save(commit=True)
                return redirect("/book-consultation#submitted")

    else:
        return render(
            request,
            "consultation.html",
            context={
                "form": ConsultationForm()
            }
        )


def faq(request):
    return render(
        request,
        "faq.html"
    )


def faq_old(request):
    return render(
        request,
        "faq-old.html"
    )

##########################################


def affliate_dashboard(request):
    if request.user.is_authenticated:
        user = request.user

        date_in_view = datetime.datetime.now()

        month_query_start_date = datetime.datetime(
            date_in_view.year,
            date_in_view.month,
            1
        )

        month_query_end_date = datetime.datetime(
            date_in_view.year,
            date_in_view.month,
            calendar.monthrange(
                date_in_view.year,
                date_in_view.month
            )[1]
        ).replace(hour=23, minute=59, second=59)

        year_query_start_date = datetime.datetime(
            date_in_view.year, 1, 1)  # First day of the current year

        year_query_end_date = datetime.datetime(
            date_in_view.year,
            12,
            31
        ).replace(hour=23, minute=59, second=59)

        # YEARLY GRAPH
        months_in_a_year = [
            'JAN',
            'FEB',
            'MAR',
            'APR',
            'MAY',
            'JUN',
            'JUL',
            'AUG',
            'SEP',
            'OCT',
            'NOV',
            'DEC'
        ]

        graph_data = []
        # Iterate through up to the current month of the year
        for (index, month) in enumerate(months_in_a_year[:date_in_view.month]):

            graph_month_query_start_date = datetime.datetime(
                date_in_view.year,
                index + 1,  # current month = Index + 1
                1  # First day of the month
            )

            graph_month_query_end_date = datetime.datetime(
                date_in_view.year,
                index + 1,
                calendar.monthrange(
                    date_in_view.year,
                    index + 1
                )[1]
            ).replace(hour=23, minute=59, second=59)

            user_earnings_this_month = UserEarnings.objects.filter(
                Q(datetime__gte=graph_month_query_start_date) & Q(
                    datetime__lte=graph_month_query_end_date),
                user=user
            ).aggregate(Sum('amount_earned'))["amount_earned__sum"] or 0,

            # Update graph Data

            graph_data.append([
                months_in_a_year[index], float(user_earnings_this_month[0])])

        return render(
            request,
            "affiliate/home.html",
            {
                "user": user,
                "month_earnings": UserEarnings.objects.filter(
                    Q(datetime__gte=month_query_start_date) & Q(
                        datetime__lte=month_query_end_date),
                    user=user
                ).aggregate(Sum('amount_earned'))["amount_earned__sum"],
                "year_earnings": UserEarnings.objects.filter(
                    Q(datetime__gte=year_query_start_date) & Q(
                        datetime__lte=year_query_end_date),
                    user=user
                ).aggregate(Sum('amount_earned'))["amount_earned__sum"],
                "number_of_referrals": len(UserEarnings.objects.filter(user=user)),
                "graph_data": graph_data
            }
        )
    else:
        return redirect("/affiliate/accounts/login")


@login_required
def affiliate_profile(request):
    user = request.user
    if request.method == "GET":
        return render(
            request,
            "affiliate/profile.html",
            {
                'profile_form': EditProfileInformation(initial={
                    'phone_number': user.profile.phone_number,
                    'full_name': user.profile.full_name,
                    'country': user.profile.country,
                    'dob': user.profile.dob,
                    'account_type': user.profile.account_type
                })
            }
        )
    elif request.method == "POST":
        form = EditProfileInformation(request.POST)
        if form.is_valid():
            profile_update_form = form.save(commit=False)
            affiliate_account = Profile.objects.get(user=request.user)
            affiliate_account.phone_number = profile_update_form.phone_number
            affiliate_account.full_name = profile_update_form.full_name
            affiliate_account.country = profile_update_form.country
            affiliate_account.dob = profile_update_form.dob
            affiliate_account.account_type = profile_update_form.account_type

            affiliate_account.save(update_fields=[
                "phone_number",
                "full_name",
                "country",
                "dob",
                "account_type"
            ])
            return redirect('affiliate-profile')


@login_required
def affiliate_transactions(request):
    user = request.user
    return render(
        request,
        "affiliate/account.html",
        {
            "transactions": UserTransactionRecord.objects.filter(user=user).order_by("-id")
        }
    )


@login_required
def vetropay_verify_account(request):
    if request.method == "GET" and request.is_ajax:
        mobile_uid = request.GET.get("userUID")

        resolve_account_response = requests.post("https://api.vetropay.com/v1/tunnel/transferfund", json={
            "publicKey": os.environ["VETROPAY_PUBLIC_KEY"],
            "privateKey": os.environ["VETROPAY_PRIVATE_KEY"],
            "mobileUID": mobile_uid,
            "amount": "10",  # test value
            "details": "Prelate Travel Ltd to {}".format(mobile_uid),
            "transferType": "standard"
        })

        return JsonResponse(resolve_account_response.json(), safe=False)


@login_required
def vetropay_fund_transfer(request):
    if request.method == "GET" and request.is_ajax:
        user = request.user
        mobile_uid = request.GET.get("userUID")
        amount = request.GET.get("amount")

        if amount <= user.balance:
            resolve_account_response = requests.post("https://api.vetropay.com/v1/tunnel/transferfund", json={
                "publicKey": os.environ["VETROPAY_PUBLIC_KEY"],
                "privateKey": os.environ["VETROPAY_PRIVATE_KEY"],
                "mobileUID": mobile_uid,
                "amount": amount,
                "details": "Prelate Travel Ltd to {}".format(mobile_uid),
                "transferType": "autocall"
            })

            response = resolve_account_response.json()
            if response["status"] == "success":
                user.balance = user.balance - decimal.Decimal(amount)
                user.save(update_fields=["balance", ])

                UserTransactionRecord.objects.create(
                    user=user,
                    transaction_type="DR",
                    amount=amount,
                    metadata="Prelate Travel Ltd to {}".format(mobile_uid)
                )

            return JsonResponse(resolve_account_response.json(), safe=False)
        else:
            return JsonResponse({"status": "failed",  "message": "Affiliate User Account Balance is insufficient"})


def term_of_service(request):
    return render(
        request,
        "term_of_service.html"
    )


def term_of_service_old(request):
    return render(
        request,
        "term_of_service_old.html"
    )


def about_us(request):
    return render(
        request,
        "about-us.html"
    )


def privacy_policy(request):
    return render(
        request,
        "privacy_policy.html"
    )


def privacy_policy_old(request):
    return render(
        request,
        "privacy_policy.html"
    )


def referral(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        referralID = request.POST.get("referralID")

        CustomerReferralRecord.objects.create(
            fullname=name, email=email, affiliate_id=referralID)

        return JsonResponse({"status": "success"}, safe=False)

    return render(
        request,
        "referral-form.html"
    )
