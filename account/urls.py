from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # TODO(mk-dv): Translate comment.
    # auth_views.PasswordChangeView проверяет форму смены пароля.
    # использует шаблон <app>/registration/password_change_form.html
    # TODO(mk-dv): Как указать путь к шаблону?
    # path(
    #     'password_change/',
    #     auth_views.PasswordChangeView.as_view(),
    #     name='password_change'
    # ),
    # auth_views.PasswordChangeDoneView отображает msg об успешной смене пароля
    # использует шаблон <app>/registration/password_change_done.html
    # TODO(mk-dv): Как указать путь к шаблону?
    # path(
    #     'password_change/done',
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name='password_change_done'
    # ),
    # Обработчики восстановления пароля
    # Производит отправку письма только if указанный email ПРИНАДЛЕЖ одному из
    # пользователей
    # path(
    #     'password_reset/',
    #     auth_views.PasswordResetView.as_view(),
    #     name='password_reset'
    # ),
    # path(
    #     'password_reset_done/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'
    # ),
    # PasswordResetView принимает uidb64 и token
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'reset/done/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'
    # ),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

]