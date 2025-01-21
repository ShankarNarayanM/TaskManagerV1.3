from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def landing_view(request):
    return render(request, "landingPage.html")

def pricing_view(request):
    return render(request,'pricingPage.html')

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        if form.is_valid():
            form.save()
            messages.success(request,'Your response is recorded')
            # return render(request,'contactPage.html')
    return render(request, 'contactPage.html')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'You have successfully created an account',{'username':username,'email':email})
            return redirect('app:loginPage')
        return render(request,'registerPage.html',{'form':form})
    return render(request,'registerPage.html')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('app:dashboardPage')
    return render(request, 'loginPage.html',{'form':form})

def dashboard_view(request):
    return render(request, 'dashBoard.html')

def logout_view(request):
    auth_logout(request)
    return redirect('app:loginPage')

