from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrForm, LoginForm

# Create your views here.

def redirect_by_role(user):
    if user.role == 'doctor':
        return '/account/dashboard'
    elif user.role == 'patient':
        return '/account/dashboard'
    else: 
        return '/admin'
    

def register_view(req):
    if req.method == 'POST':
        form = RegistrForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect(redirect_by_role(user))
    else:
        form = RegistrForm()
    return render(req, 'accounts/register.html',{'form':form})


def login_view(req):
    if req.method == 'POST':
        form = LoginForm(req, data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    return render(req, 'accounts/login.html', context)


def logout_view(req):
    logout(req)
    return redirect ('/account/login/')


@login_required  #decorators redirects them to the login page, if without being logged in
def dashboard_view(req):
    return render(req, 'accounts/dashboard.html')

