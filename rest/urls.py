from django.urls import path
from rest import views

urlpatterns = [
    path('graph/test/', views.getGraph),
]

