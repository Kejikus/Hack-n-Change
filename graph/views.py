from django.shortcuts import render


def graph_view(request):
    return render(request, "graph_test.html")

def graph_id_view(request):
    return render(request, "graph_test_id.html")