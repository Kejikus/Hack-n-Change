from django.urls import path
from rest import views

urlpatterns = [
    path('graph-data/', views.getGraph),
    path('graph-data/<int:id>/', views.getGraphId),
]

