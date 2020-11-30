from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def edit(request):
    """
    Save profile changes.

    Args:
        request (HttpRequest):
            Request with user profile data passed with the `GET` method.

    Returns:
        An `HttpResponse` with search results.
    """

    if request.method == 'POST':
        # Apparently, `<form> .__ call __ ()` can take named arguments
        # `instance` and `data`. (Yes, I know this is an obvious comment)
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        'account/edit.html',
        {'user_form': user_form, 'profile_form': profile_form}
    )


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    """
    Register new user.

    Args:
        request (HttpRequest):
            Request with user `name`, `first_name` and `password` passed with
             the `GET` method.

    Returns:
        An `HttpResponse` with search results.
    """

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # By using `User` from` django.contrib.auth`, the password
            # is stored in the database in an encrypted form (contains a prefix
            # with a part `_sha256`) -` set_password` encrypts the password.
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # Create a blank profile.
            Profile.objects.create(user=new_user)

            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user}
            )
    else:
        # The form contains either input fields, data fields, or additional
        # tags with errors.
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
