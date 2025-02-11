from django.shortcuts import render


def justview(request):
    return render(request, 'home.html', {'home': 'home'})

def bioview(request):
    return render(request, 'bio.html', {'bio': 'bio'})

def paperview(request):
    return render(request, 'paper.html', {'paper': 'paper'})

def plasticview(request):
    return render(request, 'plastic.html', {'plastic': 'plastic'})

def factoryview(request):
    return render(request, 'factory.html', {'factory': 'factory'})

def yardview(request):
    return render(request, 'yard.html', {'yard': 'yard'})

def medicalview(request):
    return render(request, 'medical.html', {'medical': 'medical'})


