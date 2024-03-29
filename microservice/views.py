from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render

from microservice.models import Microservice, Employee, Update
from microservice.utils import Status


def index(request):
    """ Главная страница """
    user: User = request.user
    if not isinstance(user, AnonymousUser):
        try:
            employee = Employee.objects.get(user=user)
            department_bound = Microservice.objects.filter(department__employee=employee)
        except Employee.DoesNotExist:
            department_bound = []
    else:
        department_bound = []

    news = [
        {
            'header': 'Новое обновление для микросервиса {}'.format(update.microservice.name),
            'body': update.description
        }

        for update in Update.objects.order_by('-date')[:10]
    ]
    context = {
        'news': news,
        'department_bound': department_bound
    }
    return render(request, 'index.html', context)


def search(request):
    user: User = request.user
    if not isinstance(user, AnonymousUser):
        try:
            employee = Employee.objects.get(user=user)
            department_bound = Microservice.objects.filter(department__employee=employee)
        except Employee.DoesNotExist:
            department_bound = []
    else:
        department_bound = []

    news = [
        {
            'header': 'Микросервис  {}'.format(update.microservice.name),
            'body': update.description
        }

        for update in Update.objects.order_by('-date')[:10]
    ]
    dev_statues = Microservice.dev_statues
    context = {
        'news': news,
        'department_bound': department_bound,
        'dev_statues': dev_statues
    }
    return render(request, 'search.html', context)

def microservice_view(request, id):
    item = None
    try:
        item = Microservice.objects.get(id=id)
    except Microservice.DoesNotExist:
        print("ыыыы")

    if item is not None:
        context = {
            'name': item.name,
            'status': dict(item.dev_statues)[Status(item.status)],
            'description': item.description,
            'business_task': item.business_task,
            'depends_on': item.depends_on.all(),
            'department': item.department,
            'tech_stack': item.tech_stack.all()
        }
        return render(request, 'microservice.html', context)


def test_view(request):
    return render(request, 'test_file.html')
