from django import forms
from .models import MoneyTransfers
from django.core.validators import RegexValidator



account_validator = RegexValidator(regex=r"^[0-9]*$")

class TransferMoneyForm(forms.ModelForm):
    from_account = forms.CharField(label='from_account', max_length=5,min_length=5,validators=[account_validator])
    to_account = forms.CharField(label='to_account', max_length=5, min_length=5, validators=[account_validator])
    amount = forms.FloatField(min_value=0.01)
    class Meta:
        model = MoneyTransfers
        fields = ("from_account","to_account","amount")
