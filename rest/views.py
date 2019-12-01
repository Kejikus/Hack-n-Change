import json

from rest_framework.decorators import api_view
from microservice.models import Microservice
from rest_framework.response import Response


@api_view(['GET'])
def getGraph(request):
    nodes = []
    edges = []
    for item in Microservice.objects.all():
        mic_name = item.name
        mic_id = item.id
        nodes.append({
            'data': {
                'id': mic_id,
                'name': mic_name
            }
        })
        for item_dep in item.depends_on.all():
            edges_id = item_dep.id
            edges.append({
                'data': {
                    'id': '{}{}'.format(mic_id, edges_id),
                    'source': mic_id,
                    'target': edges_id
                }
            })
    nodes.extend(edges)
    return Response(json.dumps(nodes))
