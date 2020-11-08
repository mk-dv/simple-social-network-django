from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Этот класс очень похож на UserCreationForm from django.contrib.auth.forms
class UserRegistrationForm(forms.ModelForm):
    # У форм реализован clean() валидирующий всю форму - используется для
    # проверки взаимосвязанных полей.
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    # TODO(mk-dv): Rename to password_repeat
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        # Эти поля будут валидироваться в соотв с типами полей модели, например
        # при вводе уже СУЩ логина - будет возбуждено exept тк в username указано
        # unique=True
        fields = ('username', 'first_name', 'email')

    # TODO(mk-dv): Возможно должен быть выше Meta
    # Можно добавлять методы clean_<field_name> к любому полю, для
    # автоматической проверки, при ошибке - она привязывается к этому полю
    # Применяется для проверки взаимосвязанных полей.
    # TODO(mk-dv): Переименовать.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise form.ValidationError("Passwords don't match.")
        return cd['password2']
