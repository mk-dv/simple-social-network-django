from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password']
            )
        # TODO(mk-dv): Translate this comment.
        # TODO(mk-dv): Check comment for grammar.
        if user is not None:
            if user.is_active:
                # TODO(mk-dv): Translate this comment.
                # Видимо здесь происходит вся магия, 'login' привязывает
                # пользователя к сессии.
                # saves the user’s ID in the session, using Django’s session framework.(middleware?)
                # Note that any data set during the anonymous session is
                # retained in the session after a user logs in.
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login or password')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # За счет использования User from django.contrib.auth пароль
            # сохраняется в бд в зашиврованном виде.(содержит префикс с частью
            # '_sha256'
            # set_password сохраняет пароль с шифрованием
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # TODO(mk-dv): Подумать над стилем.
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        # Форма содержит либо поля для ввода, либо поля с данными либо дополни
        # тельные теги с ошибками.
    return render(request, 'account/register.html', {'user_form': user_form})