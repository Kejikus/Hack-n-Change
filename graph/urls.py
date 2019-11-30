from django.contrib import admin
from django.urls import path, include

from graph import views

urlpatterns = [
    path('', views.graph_view)
]