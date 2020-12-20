from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    # POST
    path('create/', views.image_create, name='create'),
    # GET
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    # POST
    path('like/', views.image_like, name='like'),
]
