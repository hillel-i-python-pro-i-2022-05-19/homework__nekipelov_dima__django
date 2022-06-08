from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('users_generator', views.users_generator)
]
