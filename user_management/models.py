from django.db import models
from localflavor.us.models import USSocialSecurityNumberField, USStateField, USZipCodeField
from django.contrib.auth.models import User, BaseUserManager

# Create your models here.

User_type = [("customer","customer"),("t1","t1"),("t2","t2"),("t3","t3")]
class ExternalUser(User):
    # suer_type
    user_type = models.CharField(max_length=10,choices=User_type)
    # SSN.
    social_security_number = USSocialSecurityNumberField()
    # First line address.
    address1 = models.CharField(max_length=128)
    # Second line address.
    address2 = models.CharField(max_length=64)
    # City.
    city = models.CharField(max_length=64)
    # State.
    state = USStateField()
    # Zip code.
    zip_code = USZipCodeField()

    # Username and password fields are already required by default.
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'social_security_number', 'address1', 'city', 'state',
                       'zip_code']
    # Keep the username field the same.
    USERNAME_FIELD = 'username'



