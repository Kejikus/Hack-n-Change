from django.shortcuts import render

from microservice.models import Microservice


def index(request):
    microservices = Microservice.objects.all()[:10]
    return render(template_name='index', context={'microservices': microservices}, request=request)

