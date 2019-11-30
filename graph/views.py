from django.shortcuts import render


def graph_view(request):
    return render(request, "graph_test.html")