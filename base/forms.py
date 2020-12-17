from django import forms
from .models import TravelInformation, TravelAssistance, TravelBudget
from .models import UsersCustomTourRequest, TourDealInterest
from allauth.account.forms import SignupForm

PROFILE_TYPE = (
    ('01', 'INIDIVDUAL'),
    ('02', 'BUSINESS')
    )


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['account_type'] = forms.ChoiceField(choices=PROFILE_TYPE)




    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        account_type = self.cleaned_data.pop('account_type')

        # Update profile Information
        user.profile.account_type = account_type
        user.profile.save(update_fields = ["account_type"])

        return user


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
