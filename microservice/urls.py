from django.urls import path

from microservice import views

urlpatterns = [
    path('', views.index, name='index'),
    path('microservice/<int:id>/', views.department_view, name='microservice'),
    path('test/', views.test_view),
]
