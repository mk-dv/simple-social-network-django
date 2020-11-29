from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    """Changing `User` fields from `django.contrib.auth.models`."""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


# This class is very similar to `UserCreationForm` from
# `django.contrib.auth.forms`.
class UserRegistrationForm(forms.ModelForm):
    # A `<Form>.clean` method validates the entire form - it is used to
    # validate related fields.
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        # These fields will be validated following the field types of the
        # model, for example, when entering an existing login - an exception
        # will be raised because a `username` specifies `unique = True`.
        fields = ('username', 'first_name', 'email')

    # You can add `clean_ <field_name>` methods for any field, for automatic
    # check, if error occurred - check is bound to this field. Is used to check
    # related fields.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
