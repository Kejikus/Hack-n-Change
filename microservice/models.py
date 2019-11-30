from enum import Enum

from django.db import models


class Microservice(models.Model):

    class Status(Enum):
        Idea = 'IDEA'
        InDev = 'INDEV'
        Test = 'TEST'
        Deployed = 'DEPLOYED'
        Deprecated = 'DEPRECATED'
        EndLife = 'ENDLIFE'

    dev_statues = (
        (Status.Idea, 'Idea'),
        (Status.InDev, 'In development'),
        (Status.Test, 'Testing'),
        ('DEPLOYED', 'Deployed'),
        ('DEPRECATED', 'Deprecated'),
        ('ENDLIFE', 'Removed (life cycle end)')
    )

    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=dev_statues, default=dev_statues[0][0])


