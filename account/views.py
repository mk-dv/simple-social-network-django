from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


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