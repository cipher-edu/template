from django.shortcuts import render
from .models import *
def home(request):
    landing = LandingHead.objects.all()
    context = {
        'landing':landing
    }

    return render(request, 'index.html', context)