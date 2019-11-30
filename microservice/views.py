from django.shortcuts import render

from microservice.models import Update


def index(request):
    microservices = Update.objects.order_by(Update.date).all()[:10]
    return render(template_name='index', context={'microservices': microservices}, request=request)

