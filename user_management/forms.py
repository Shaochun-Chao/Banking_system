from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExternalUser
from django.core.validators import RegexValidator
from django.forms.fields import EmailField
from localflavor.us.forms import USSocialSecurityNumberField, USStateSelect, USZipCodeField

username_validator = RegexValidator(regex=r"^[a-z]([a-z0-9]|_){1,31}",message=('Please enter a valid username. '
'A username must be between 2 and 32 characters, starting with a lowercase letter, and only including lowercase letters, numbers, and underscores'))
# Allow for Mike, LeAnn, Kay'La, and John-Paul (Max 32 total characters).
first_name_validator = RegexValidator(regex=r"^[A-Z]([a-zA-Z]|\-|'){1,31}")
# Allow for Stevens, McDonald, O'Brien, and O'Brien-Stevens (Max 64 total characters).
last_name_validator = RegexValidator(regex=r"^[A-Z]([a-zA-Z]|\-|'){1,63}")

class LoginForm(forms.Form):
    '''
    Form class handling the login information.
    '''

    username = forms.CharField(label='Username', max_length=128)
    password = forms.CharField(label='Password', max_length=128)#, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(initial=False,required=False)


class RegistrationForm(UserCreationForm):
    def clean_email(self):
        # Get the email.
        email = self.cleaned_data.get('email')
        try:
            # Check if it exists
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        # User was found with this email, raise an error.
        raise forms.ValidationError('Email already in use. Please try another.')

    # Username used to log in.
    username = forms.CharField(label='Username', min_length=2, max_length=32, required=True, validators=[username_validator], error_messages={'required': 'You must fill out your username.'})
    # Collect passwords.
    password1 = forms.CharField(label='Password',min_length=8, max_length=128, required=True, widget=forms.PasswordInput, error_messages={'required': 'You must fill out your password.'})
    password2 = forms.CharField(label='Confirm password',min_length=8, max_length=128, required=True, widget=forms.PasswordInput, error_messages={'required': 'You must confirm your password.'})
    # Email address.
    email = EmailField(label='Email address', max_length=64, required=True, error_messages={'required': 'You must fill out your email address.'})
    # User's first name. Will limit to only 32 chars, starting with capitol and containing ' or -.
    first_name = forms.CharField(label='First Name', max_length=32, required=True, validators=[first_name_validator], error_messages={'required': 'You must fill out your first name.'})
    # User's last name. Same rules as first name, but with 64 chars.
    last_name = forms.CharField(label='Last Name', max_length=64, required=True, validators=[last_name_validator], error_messages={'required': 'You must fill out your last name.'})
    # Collect SSN (valid example is 586-54-1541).
    social_security_number = USSocialSecurityNumberField(label='Social Security Number', required=True, initial="586-54-1541", error_messages={'required': 'You must fill out your SSN.'})
    # First line address.
    address1 = forms.CharField(label='Address Line 1', max_length=128, required=True, initial="699 S. Mill Ave.", error_messages={'required': 'You must fill out your address line 1.'})
    # Second line address.
    address2 = forms.CharField(label='Address Line 2', max_length=64, required=False)
    # City.
    city = forms.CharField(label='City', max_length=64, required=True, initial="Tempe", error_messages={'required': 'You must fill out your city.'})
    # State.
    state = forms.CharField(widget=USStateSelect, required=True, initial="AZ", error_messages={'required': 'You must fill out your state.'})
    # Zip code.
    zip_code = USZipCodeField(label='Zip Code', required=True, initial="85281", error_messages={'required': 'You must fill out your zip code.'})
    class Meta:
        model = ExternalUser
        fields = ('username', 'email', 'first_name', 'last_name', 'social_security_number', 'address1', 'city', 'state', 'zip_code')

# class FundTransactionForm(forms.ModelForm):
#
#     from_account = forms.CharField(label='from account',min_length=5,max_length=5,required=True)
#     to_account = forms.CharField(label='to account',min_length=5,max_length=5,required=True)
#     amount = forms.FloatField(required=True)
#
#     class Meta:
