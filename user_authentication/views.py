from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Retrieve the user object after validation
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page or a dashboard
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')