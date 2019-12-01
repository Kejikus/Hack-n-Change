from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Microservice


# @registry.register_document
# class MicroserviceDocument(Document):
#     class Index:
#         name = 'microservices'
#
#         settings = {
#             'number_of_shards': 1,
#             'number_of_replicas': 0
#         }
#
#     class Django:
#         model = Microservice
#
#         fields = [
#             'name',
#             'status',
#             'description',
#             'business_task',
#         ]