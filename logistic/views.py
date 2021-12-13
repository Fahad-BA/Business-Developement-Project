from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from logistic.forms import OrderForm, RegistrationForm, AccountUpdateForm
from logistic.models import Tracking, Orders, Package
from django.db import IntegrityError
from django.http import HttpResponse
from django.utils import timezone
from django.conf import settings


# Main Pages
def home(request):
        return render(request, 'logistic/home.html')

def about(request):
    return render(request, 'logistic/about.html')

def story(request):
    return render(request, 'logistic/ourstory.html')

def support(request):
	if request.method=='POST':
		message = request.POST['message'],
		send_mail("Customer's message",
			message,
			settings.EMAIL_HOST_USER,
			['fhidan@outlook.com'],
			fail_silently=False)
	return render(request, 'logistic/support.html')

def support_success(request):
    return render(request, 'logistic/support_success.html')

#Users Pages
def signupuser(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['Registration_Form'] = form 
    else:
        form = RegistrationForm()
        context['Registration_Form'] = form
    return render(request, 'logistic/signupuser.html', context)

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'logistic/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'logistic/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and Password did not match.'})
        else:
            login(request, user)
            return redirect('home')    

def logoutuser(request):
    logout(request)
    return redirect('home')

# Services Pages
def tracking(request):
    if 'Track' in request.GET:
        Track = request.GET['Track']
        shipments = Tracking.objects.filter(Shipment_Number__icontains=Track)
        return render(request, 'logistic/tracking.html', {'shipments':shipments})

    else:
        Error = "Please enter a valid tracking number."
        return render(request, 'logistic/tracking.html', {'Error':Error})

def orders(request):
    if request.method == 'GET':
        return render(request, 'logistic/orders.html', {'form':OrderForm()})

    else:
        try:
            form = OrderForm(request.POST)
            neworder = form.save(commit=False)
            neworder.user = request.user
            neworder.save()
            return redirect(order_success)
        except ValueError:
            return render(request, 'logistic/orders.html', {'form':OrderForm(), 'error':'Bad Data Passed In. Try Again.'})

def order_success(request):
    return render(request, 'logistic/order_success.html')

def shipments(request):
    return render(request, 'logistic/shipments.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect(loginuser)
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, isinstance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial = {
                "email":request.user.email,
                "username":request.user.username,
            }
        )

        context['account_form'] = form

    return render(request, 'logistic/profile.html', context)

def address(request):
    return render(request, 'logistic/address.html')

def Packs(request):
    Packs = Package.objects.all()
    context = {'Packs':Packs}
    return render(request, 'logistic/Packages.html', context)