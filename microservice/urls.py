from django.urls import path

from microservice import views

urlpatterns =[
    path('', views.index),
]