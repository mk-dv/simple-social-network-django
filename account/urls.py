from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    # The page for new user registration.
    path('register/', views.register, name='register'),
    # The page for editing user profile data.
    path('edit/', views.edit, name='edit'),
]
