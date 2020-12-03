from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    # REST POST
    path('create/', views.image_create, name='create'),
]
