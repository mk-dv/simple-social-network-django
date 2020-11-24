from django.urls import path, include

from . import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # An `auth_views.PasswordChangeView` validates the password change form,
    # and uses the template `<app>/registration/password_change_form.html`.
    # path(
    #     'password_change/',
    #     auth_views.PasswordChangeView.as_view(),
    #     name='password_change'
    # ),
    # An `auth_views.PasswordChangeDoneView` displays a message about
    # successful password change using the template
    # `<app>/registration/password_change_done.html`.
    # path(
    #     'password_change/done',
    #     auth_views.PasswordChangeDoneView.as_view(),
    #     name='password_change_done'
    # ),

    # Password recovery paths.

    # Sends an email only if the specified email belongs to one of the existing
    # users.
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
    # PasswordResetView gets kwargs `uidb64` and `token`.
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
    path('edit/', views.edit, name='edit'),
]
