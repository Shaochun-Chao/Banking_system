from django.shortcuts import render,redirect
#from django.contrib.auth.decorators import login_required
# Create your views here.
from user_management.models import ExternalUser

#@login_required
def login(request):
    return redirect('accounts/login')

def homepage(request):
    context = {}


    #print("homepage:", username)
    #context['user_type'] = username
    username = request.user.username
    currentsuer = ExternalUser.objects.get(username=username)
    context['user_type'] = currentsuer.user_type
    return render(request,'homepage.html',context)