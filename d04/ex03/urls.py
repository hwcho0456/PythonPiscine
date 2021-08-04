from django.urls import path

from . import views

urlpatterns = [
    path('', views.Ex03.as_view(), name='ex03'),
]