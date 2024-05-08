from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages

# Create your views here.

# ************************************************************
# Login page
# ************************************************************
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zakończyło się sukcesem.')
                else:
                    return HttpResponse('Konto jest zablokowane.')
            else:
                return HttpResponse('Nieprawidłowe dane uwierzytelniające.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


# ************************************************************
# Registration
# ************************************************************
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Utworzenie nowego obiektu użytkownika; jednak jeszcze nie zapisujemy go w bazie danych.
            new_user = user_form.save(commit=False)
            # Ustawienie wybranego hasła.
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Zapisanie obiektu User.
            new_user.save()
            # Utworzenie profilu użytkownika.
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


# ************************************************************
# Account page
# ************************************************************
@login_required
def details(request):
    return render(request, 'account/details.html')

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Uaktualnienie profilu '\
                                     'zakończyło się sukcesem')
        else:
            messages.error(request, 'Wystąpił błąd podczas uaktualniania profilu.')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})



# ************************************************************
# Dashboard
# ************************************************************
@login_required
def dashboard(request):
    return render(request, 'dashboard/panel.html')

@login_required
def empty(request):
    return render(request, 'dashboard/empty.html')


# ************************************************************
# Homepage
# ************************************************************
def home(request):
    return render(request, 'pages/home.html')