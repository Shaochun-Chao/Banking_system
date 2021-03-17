from django.contrib import admin
from .models import ExternalUser
from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(ExternalUser)
admin.site.unregister(Group)