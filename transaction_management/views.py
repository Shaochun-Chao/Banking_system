from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TransferMoneyForm
from django.views.generic import TemplateView
from account_management.models import Account
from user_management.models import ExternalUser

# incomplete
def transfer(request):
    context = {}
    # print(request.user.get_username())
    # form = TransferMoneyForm(request.POST)
    if request.POST:
        # print("POST")
        # print(form)
        # print("from account:",request.POST['from_account'])
        context = {}

        try:
            from_account = Account.objects.get(account_number=request.POST['from_account'])
        except:

            # form = TransferMoneyForm
            context['from_account_not_exist'] = True
            context['user_type'] = request.user.get_username()
            return render(request, 'transfer.html', context)

        try:
            to_account = Account.objects.get(account_number=request.POST['to_account'])
        except:
            context['to_account_not_exist'] = True
            username = request.user.username
            currentsuer = ExternalUser.objects.get(username=username)
            context['user_type'] = currentsuer.user_type
            return render(request, 'transfer.html', context)
        # print("from account balance:", from_account.account_balance)
        # print("to account balance", to_account.account_balance)
        if float(request.POST['amount']) > float(from_account.account_balance):
            context['from_account_not_enough_money'] = True
            username = request.user.username
            currentsuer = ExternalUser.objects.get(username=username)
            context['user_type'] = currentsuer.user_type
            return render(request, 'transfer.html', context)
       #rint("dif:", float(from_account.account_balance)- float(request.POST['from_account']))
        from_account.account_balance =  str(float(from_account.account_balance) - float(request.POST['amount']))
        to_account.account_balance =  str(float(to_account.account_balance) + float(request.POST['amount']))
        from_account.save()
        to_account.save()
        # print("after:")
        # print("from account balance:", from_account.account_balance)
        # print("to account balance", to_account.account_balance)
        username = request.user.username
        currentsuer = ExternalUser.objects.get(username=username)
        context['user_type'] = currentsuer.user_type
        # form = TransferMoneyForm
        return render(request, 'transfer.html', context)
    else:
        #context = {}
        username = request.user.username
        currentsuer = ExternalUser.objects.get(username=username)
        user_type = currentsuer.user_type
        form = TransferMoneyForm

        return render(request, 'transfer.html', {'form': form, 'user_type': user_type})
