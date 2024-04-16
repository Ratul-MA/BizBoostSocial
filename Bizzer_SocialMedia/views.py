from django.shortcuts import render, redirect
from django.contrib import messages
from FA_overview.models import Profile
from FA_overview.models import Beep
from FA_overview.forms import BeepForm, SignUpForm, ProfilePicForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404


def whitepaper(request):
    return render(request, "Bwhitepaper.html")


def PlatformOverview(request):
    return render(request, "Platform Overview.html")


def product(request):
    return render(request, "product.html")


def Bizzer(request):
    if request.user.is_authenticated:
        form = BeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                beep = form.save(commit=False)
                beep.user = request.user
                beep.save()
                messages.success(request, ("Your beep Has Been Posted!"))
                return redirect('base.html')

        beeps = Beep.objects.all().order_by("-created_at")
        return render(request, 'Bizzer.html', {"beeps": beeps, "form": form})
    else:
        beeps = Beep.objects.all().order_by("-created_at")
        return render(request, 'Bizzer.html', {"beeps": beeps})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profiles})
    else:
        messages.success(request, 'You are not logged in')
        return redirect('Bizzer')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        beeps = Beep.objects.filter(user_id=pk).order_by("-created_at")

        # Post Form logic
        if request.method == "POST":
            # Get current user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            # Save the profile
            current_user_profile.save()

        return render(request, "profile.html", {"profile": profile, "beeps": beeps})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('Bizzer')


def followers(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)
            return render(request, 'followers.html', {"profiles": profiles})
        else:
            messages.success(request, ("That's Not Your Profile Page..."))
            return redirect('Bizzer')
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('Bizzer')


def follows(request, pk):
    if request.user.is_authenticated:
        if request.user.id == pk:
            profiles = Profile.objects.get(user_id=pk)
            return render(request, 'follows.html', {"profiles": profiles})
        else:
            messages.success(request, ("That's Not Your Profile Page..."))
            return redirect('Bizzer')
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('Bizzer')


def unfollow(request, pk):
    if request.user.is_authenticated:
        # Get the profile to unfollow
        profiles = Profile.objects.get(user_id=pk)
        # Unfollow the user
        request.user.profile.follows.remove(profiles)
        # Save our profile
        request.user.profile.save()

        # Return message
        messages.success(request, (f"You Have Successfully Unfollowed {profiles.user.username}"))
        return redirect(request.META.get("HTTP_REFERER"))

    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        # Get Forms
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            login(request, current_user)
            messages.success(request, ("Your Profile Has Been Updated!"))
            return redirect('profile.html')

        return render(request, "update_user.html", {'user_form': user_form, 'profile_form': profile_form})
    else:
        messages.success(request, ("You Must Be Logged In To View That Page..."))
        return redirect('Bizzer')


def beep_like(request, pk):
    if request.user.is_authenticated:
        beep = get_object_or_404(Beep, id=pk)
        if beep.likes.filter(id=request.user.id):
            beep.likes.remove(request.user)
        else:
            beep.likes.add(request.user)

        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("You Must Be Logged In To View That Page..."))
        return redirect('Bizzer')


def beep_show(request, pk):
    beep = get_object_or_404(Beep, id=pk)
    if beep:
        return render(request, "show_beep.html", {'beep': beep})
    else:
        messages.success(request, ("That beep Does Not Exist..."))
        return redirect('Bizzer')


def delete_beep(request, pk):
    if request.user.is_authenticated:
        beep = get_object_or_404(Beep, id=pk)
        # Check to see if you own the beep
        if request.user.username == beep.user.username:
            # Delete The beep
            beep.delete()

            messages.success(request, ("The beep Has Been Deleted!"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.success(request, ("You Don't Own That beep!!"))
            return redirect('Bizzer')

    else:
        messages.success(request, ("Please Log In To Continue..."))
        return redirect(request.META.get("HTTP_REFERER"))


def edit_beep(request, pk):
    if request.user.is_authenticated:
        # Grab The beep!
        beep = get_object_or_404(Beep, id=pk)

        # Check to see if you own the beep
        if request.user.username == beep.user.username:

            form = BeepForm(request.POST or None, instance=beep)
            if request.method == "POST":
                if form.is_valid():
                    beep = form.save(commit=False)
                    beep.user = request.user
                    beep.save()
                    messages.success(request, ("Your beep Has Been Updated!"))
                    return redirect('base.html')
            else:
                return render(request, "edit_beep.html", {'form': form, 'beep': beep})

        else:
            messages.success(request, ("You Don't Own That beep!!"))
            return redirect('profile.html')

    else:
        messages.success(request, ("Please Log In To Continue..."))
        return redirect('base.html')


def search(request):
    if request.method == "POST":
        # Grab the form field input
        searches = request.POST['search']
        # Search the database
        searched = Beep.objects.filter(body__contains=searches)

        return render(request, 'search.html', {'search': searches, 'searched': searched})
    else:
        return render(request, 'search.html', {})
