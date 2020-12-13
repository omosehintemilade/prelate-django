from django import forms
from .models import Profile


class EditProfileInformation(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'full_name', 'country', 'dob', 'account_type')
