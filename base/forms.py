from django import forms
from .models import TravelInformation, TravelAssistance, TravelBudget
from .models import UsersCustomTourRequest, TourDealInterest


class TravelInformationForm(forms.ModelForm):
    class Meta:
        model = TravelInformation
        fields = "__all__"


class TravelAssistanceForm(forms.ModelForm):
    class Meta:
        model = TravelAssistance
        fields = "__all__"


class TravelBudgetForm(forms.ModelForm):
    class Meta:
        model = TravelBudget
        fields = "__all__"


class UsersCustomTourRequestForm(forms.ModelForm):
    class Meta:
        model = UsersCustomTourRequest
        fields = "__all__"


class TourDealInterestForm(forms.ModelForm):
    class Meta:
        model = TourDealInterest
        fields = "__all__"
