from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    hcontent = LandingHead.objects.all()
    context = {
        'hcontent': hcontent
    }
    return render(request, 'index.html', context)