from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('moneytransfer/', views.transfer, name="view_accounts"),
    #path('open_account/', views.open_accounts, name="view_accounts"),
]