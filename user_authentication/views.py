from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, ProfileForm
from django.views.generic import UpdateView
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Authentication 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with your login URL name
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')  # Redirect to your home page or another page
    else:
        form = LoginForm()  # Create an empty form for GET requests

    return render(request, 'auth/login.html', {'form': form})  # Pass the form to the template

def user_logout(request):
    logout(request)
    return render(request, 'auth/logout.html')



# Profile

@login_required
def profile_view(request):
    """
    Display the profile page.
    """
    profile = request.user.profile  # Access the related profile
    return render(request, 'user_profile/profile.html', {'profile': profile})

@login_required
def edit_profile_view(request):
    """
    Edit the user's profile.
    """
    profile = request.user.profile  # Access the related profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')  # Redirect to the profile view
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'user_profile/edit_profile.html', {'form': form})