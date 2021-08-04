from django.urls import path

from . import views

urlpatterns = [
    path('', views.Ex02.as_view(), name='ex02'),
]