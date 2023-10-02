from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('old', views.homeOld, name="home-old"),
    path('reservations', views.reservations, name="reservations"),
    path('travel-help-old', views.travel_helpOld, name="travel-help-old"),
    path('travel-help', views.travel_help, name="travel-help"),
    path('travel-info', views.travel_info, name="travel-info"),
    path('travel_assistance', views.travel_assistance, name="travel-assistance"),
    path('request-change', views.request_change, name="request-change"),
    path('travel_budget', views.travel_budget, name="travel_budget"),
    path('travel-insurance', views.travel_insurance, name="travel-insurance"),
    path('travel-insurance-old', views.travel_insuranceOld,
         name="travel-insurance-old"),
    path('visa-assistance', views.visa_assistance, name="visa-assistance"),
    path('visa-assistance-old', views.visa_assistance_old,
         name="visa-assistance-old"),
    path('post-arrival-services', views.post_arrival_services,
         name="post-arrival-services"),
    path('tour', views.tour, name="tour"),
    path('tour-old', views.tourOld, name="tour-old"),
    path('tour/<int:pk>/<slug:slug>', views.tour_deal, name="tour-deal"),
    path('tour-old/<int:pk>/<slug:slug>',
         views.tour_deal_old, name="tour-deal-old"),
    path('tour/customize-old', views.customize_tourOld, name="customize-tour-old"),
    path('tour/customize', views.customize_tour, name="customize-tour"),
    path('business-travel', views.business_travel, name="business-travel"),
    path('business-travel-old', views.business_travel_old,
         name="business-travel-old"),
    path('become-affiliate', views.become_affiliate, name="become-affiliate"),
    path('become-affiliate-old', views.become_affiliate_old,
         name="become-affiliate-old"),
    path("contact-us", views.contact_us, name="contact-us"),
    path("contact-us-old", views.contact_us_old, name="contact-us-old"),
    path("book-consultation", views.book_consultation, name="book-consultation"),
    path("faq", views.faq, name="faq"),
    path("faq-old", views.faq_old, name="faq-old"),
    path("affiliate/dashboard", views.affliate_dashboard,
         name="affliate_dashboard"),
    path("affiliate/accounts/", include('allauth.urls')),
    path("affiliate/profile", views.affiliate_profile, name="affiliate-profile"),
    path("affiliate/transactions", views.affiliate_transactions,
         name="affiliate-transactions"),
    path('vetropay-verify-account',
         views.vetropay_verify_account, name='verify-account'),
    path('vetropay-mobile-transfer',
         views.vetropay_fund_transfer, name='transfer-fund'),
    #
    path('term-of-service-old', views.term_of_service_old,
         name="term-of-service-old"),
    path('about-us', views.about_us, name="about-us"),
    path('term-of-service', views.term_of_service, name="term-of-service"),
    path('privacy-policy', views.privacy_policy, name="privacy-policy"),
    path('privacy-policy-old', views.privacy_policy_old, name="privacy-policy-old"),
    path('referrals', views.referral, name="referral"),
    path('newsletters', views.subscribe_to_newsletter, name="newsletters")

]
