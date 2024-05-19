from django.shortcuts import render


def index(request):
    """The home page for Pizza placing website"""
    return render(request, 'pizzas/index.html')
