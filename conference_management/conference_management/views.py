from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group
from .forms import UserRegistrationForm, LoginForm
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile.objects.create(
                user=user,
                role=form.cleaned_data['role'],
                country_region=form.cleaned_data['country_region'],
                google_scholar_id=form.cleaned_data['google_scholar_id'],
                semantic_scholar_id=form.cleaned_data['semantic_scholar_id'],
                dblp_id=form.cleaned_data['dblp_id'],
                orcid_id=form.cleaned_data['orcid_id'],
                open_review_id=form.cleaned_data['open_review_id']
            )
            # Assign the user to appropriate groups based on role
            group_name = form.cleaned_data['role']
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
            else:
                return render(request, '/registration/login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
            else:
                return render(request, '/registration/login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    role = user_profile.role
    if role == 'chair':
        return render(request, 'dashboard/dashboard_chair.html', {'user_profile': user_profile})
    elif role == 'author':
        return render(request, 'dashboard/dashboard_author.html', {'user_profile': user_profile})
    elif role == 'reviewer':
        return render(request, 'dashboard/dashboard_reviewer.html', {'user_profile': user_profile})
    else:
        return render(request, 'unauthorized.html')

#username=abc    
#password=idW7VuR3kyi4UES


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

