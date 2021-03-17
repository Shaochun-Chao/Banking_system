from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
from django.views.generic import TemplateView
from .models import ExternalUser

# Create your views here.
# def login(request):
#     return render(request, 'login.html')


def loginn(request):
    context = {}

    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data['username']
        #print("username:", username)

    if request.POST:
        # need to store the user type in the context["user_type"]
        # 1 is for customer; 2 is for t1 employee; 3 is for employee; it can modify in homepage.html
        # here just take customer for example
        # if form.cleaned_data['username']=='1':
        if form.is_valid():
            # Get the username.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            # Display in log and return.
            #print('Found username: {username} and password {password}. Remember me? = {remember_me}')
            user = authenticate(username=username, password=password)
            #print("user:",user)
            if user is not None:
                login(request, user)
                currentsuer = ExternalUser.objects.get(username = username)
                #print("curr:",currentsuer.user_type)

                context["user_type"] = currentsuer.user_type
                print("redirect")
                #return render(request,'/homepage.html')
                return redirect('/homepage')
            return render(request, 'login.html', {'form': form})
            # return HttpResponseRedirect('/login/')
            # return render(request,'homepage.html', context)
        # elif form.cleaned_data['username']=='2':
        #     context["user_type"] = '2'
        #     user = authenticate(username='2', password='e5522333')
        #     login(request, user)
        #     return render(request,'homepage.html', context)
        # elif form.cleaned_data['username']=='3':
        #     context["user_type"] = '3'
        #     user = authenticate(username='3', password='e5522333')
        #     login(request, user)
        #     return render(request,'homepage.html', context)
        # elif form.cleaned_data['username']=='4':
        #     context["user_type"] = '4'
        #     user = authenticate(username='4', password='e5522333')
        #     login(request, user)
        #     return render(request,'homepage.html', context)
    else:
        if request.user.is_authenticated:
            # print(form.cleaned_data['username'])
            print("GOT IT HERE")
            return render(request, 'login.html', {'form': form})
        print("NOT AUTHED!")
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    print("loginn")

    return render(request, 'login.html')


def register(request):
    context = {}
    form = RegistrationForm(request.POST)
    if request.POST:
        print("reg POST")
        if form.is_valid():
            form.save()
            # Get the information.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            ssn = form.cleaned_data['social_security_number']
            # Display in log and return.
            print(f'Found username: {username}, password: {password}, '
                  f'first name: {first_name}, last name: {last_name}, ssn: {ssn}')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            form = LoginForm()
            return render(request, 'login.html', {'form': form})
            # return redirect('/')

        # for f in form:
        #     for error in f.errors:
        #         print(error)
    else:
        if request.user.is_authenticated:
            print("GOT REGISTER HERE")
            return render(request, 'register.html', {'form': form})
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    # print("1234")
    logout(request)
    context = {}
    print(request.user)
    return redirect('login')
