from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('travel-help', views.travel_help, name="travel-help"),
    path('travel-insurance', views.travel_insurance, name="travel-insurance"),
    path('visa-assistance', views.visa_assistance, name="visa-assistance"),
    path('tour', views.tour, name="tour"),
    path('tour/<int:pk>/<slug:slug>', views.tour_deal, name="tour-deal"),
    path('tour-package-customize', views.customize_tour, name="customize-tour"),
    path('business-travel', views.business_travel, name="business-travel"),
    path('become-affiliate', views.become_affiliate, name="become-affiliate"),
    path("contact-us", views.contact_us, name="contact-us"),
    path("faq", views.faq, name="faq")
    
]