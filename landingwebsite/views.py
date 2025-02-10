from django.shortcuts import render


def justview(request):
    return render(request, 'base.html', {'home': 'home'})

