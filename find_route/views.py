from django.shortcuts import render


def home(request):
    name = 'Vladimir'
    return render(request, 'home.html', {'name': name})
