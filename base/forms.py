from django import forms
from .models import TravelInformation, TravelAssistance, TravelBudget
from .models import UsersCustomTourRequest, TourDealInterest
from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['full_name'] = forms.CharField(required=True)
        self.fields['country'] = forms.CharField(required=True)
        self.fields['dob'] = forms.DateField(required=True)
        self.fields['phone_number'] = forms.CharField(required=True)




    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        full_name = self.cleaned_data.pop('full_name')


class TravelInformationForm(forms.ModelForm):
    class Meta:
        model = TravelInformation
        fields = "__all__"


class TravelAssistanceForm(forms.ModelForm):
    class Meta:
        model = TravelAssistance
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TravelAssistanceForm, self).__init__(*args, **kwargs)
        self.fields['document'].required = False


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
