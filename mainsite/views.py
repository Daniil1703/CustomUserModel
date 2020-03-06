from django.shortcuts import render


def index(request):
    return render(request, 'mainsite/includes/index.html', context=None)
