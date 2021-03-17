from django.shortcuts import render
from user_management.models import ExternalUser
# Create your views here.
def view_accounts(request):

    context = {}
    #print(request.user)
    username = request.user.username
    currentsuer = ExternalUser.objects.get(username=username)
    context['user_type'] = currentsuer.user_type
    #account = Account.objects.filter(user_id = request.user.get_username())
    #print(account)
    return render(request, 'view_account.html',context)

def open_accounts(request):

    context = {}
    username = request.user.username
    currentsuer = ExternalUser.objects.get(username=username)
    context['user_type'] = currentsuer.user_type
    return render(request, 'open_accounts.html',context)