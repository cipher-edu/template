from django.shortcuts import render
from .models import *
def home(request):
    landing = LandingHead.objects.all()
    postl = Postl.objects.all()
    postr = Postr.objects.all()
    context = {
        'landing':landing,
        'postl': postl,
        'postr': postr,
    }

    return render(request, 'index.html', context)
def blog(request):
    # archive = Postarchive.objects.all()
    category = request.GET.get('category')
    if category == None:
        archive = Postarchive.objects.all()
    else:
        archive = Postarchive.filter(category=category)
    context = {
        'archive':archive
    }
    return render(request, 'blog.html', context)

def cat(request):
    return render(request, 'category.html')