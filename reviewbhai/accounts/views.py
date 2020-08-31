from django.shortcuts import render,redirect
from .models import Account
from .forms import RegistrationForm, LogInForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_view(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}.')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.method=='POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form =LogInForm()
    return render(request,'accounts/login.html',{'form': form})

@login_required
def profile_view(request,username):
    user = Account.objects.get(username = username)
    context = {
        'object' : user,
    }
    template_name = 'accounts/profile.html'
    return render(request,template_name,context)

@login_required
def updateprofile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Information Updated')
            return redirect('profile',request.user.username)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }
    return render(request,'accounts/update_profile.html',context)