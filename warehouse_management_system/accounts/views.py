from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, AccountForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    #auth_user = request.user.username # , {'auth_user':auth_user}
    return render(request, 'accounts/home.html')

def registration(request):
    registered = False
    if request.method == 'POST':
        reg_form = RegistrationForm(data=request.POST)
        acc_form = AccountForm(data=request.POST)

        if reg_form.is_valid() and acc_form.is_valid():
            user = reg_form.save()
            user.set_password(user.password)
            user.save()

            acc = acc_form.save(commit=False)
            acc.user = user

            if 'profile_pic' in request.FILES:
                acc.profile_pic = request.FILES['profile_pic']
            
            acc.save()

            registered = True
        else:
            print(reg_form.errors, acc_form.errors)
    else:
        reg_form = RegistrationForm()
        acc_form = AccountForm()
    return render(request, 'accounts/registration.html', 
                  {'reg_form': reg_form, 
                   'acc_form': acc_form, 
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect(reverse('home'), {'user':user})
                return redirect('home')
            
            else:
                return HttpResponse('Your account is not active')
        
        else:
            print('Someone tries to login and failed.')
            print('Username {} and password {}'.format(username, password))
            return HttpResponse('Invalid login information provided.')
    else:
        return render(request, 'accounts/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))