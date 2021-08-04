from django.urls import path

from . import views

urlpatterns = [
    path('<str:template>', views.Ex01.as_view(), name='ex01'),
]