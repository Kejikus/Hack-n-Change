from enum import Enum

from django.contrib.auth.models import User
from django.db import models

from microservice.utils import Status


class Microservice(models.Model):

    dev_statues = (
        (Status.Idea, 'Прототип'),
        (Status.InDev, 'В разработке'),
        (Status.Testing, 'Тестируется'),
        (Status.Deployed, 'Используется'),
        (Status.Deprecated, 'Устарел'),
        (Status.Removed, 'Не используется')
    )

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=dev_statues, default=dev_statues[0][0])
    description = models.TextField()
    business_task = models.CharField(max_length=100)
    depends_on = models.ManyToManyField("Microservice", "dependants", "dependants",
                                        through="MicroserviceBind")  # Связь этого микросервиса с другими
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    tech_stack = models.ManyToManyField("Technology", "microservices", "microservices",
                                        through="MicroserviceTechnology")


class MicroserviceBind(models.Model):

    dependant = models.ForeignKey("Microservice", on_delete=models.CASCADE, related_name='depends_on_binds')
    depends_on = models.ForeignKey("Microservice", on_delete=models.CASCADE, related_name='dependants_binds')
    description = models.CharField(max_length=20, blank=True, default="")


class Department(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    @property
    def email(self):
        return self.user.email

    @email.setter
    def email(self, value):
        self.user.email = value

    @property
    def first_name(self):
        return self.user.first_name

    @first_name.setter
    def first_name(self, value):
        self.user.first_name = value

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)
        self.user.save()


class Technology(models.Model):

    name = models.CharField(max_length=20)


class MicroserviceTechnology(models.Model):

    microservice = models.ForeignKey("Microservice", on_delete=models.CASCADE)
    technology = models.ForeignKey("Technology", on_delete=models.CASCADE)


class Issue(models.Model):

    header = models.CharField(max_length=100)
    description = models.TextField()
    microservice = models.ForeignKey("Microservice", on_delete=models.CASCADE)


class Update(models.Model):

    description = models.TextField()
    microservice = models.ForeignKey("Microservice", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

