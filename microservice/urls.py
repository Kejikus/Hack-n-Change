from django.urls import path

from microservice import views

app_name = 'microservices'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('microservice/<int:id>/', views.microservice_view, name='microservice'),
]
