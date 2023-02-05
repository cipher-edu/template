from django.shortcuts import render, HttpResponse, get_object_or_404
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

def show_post(request, post_id):
    post = get_object_or_404(Postarchive, pk=post_id)
    context = {
        'post':post,
        'cat_selected':post_id

    }
    return render(request, 'post.html', context=context)
    
def categories(request, catid):
    return HttpResponse(f"<p>sizga kk sahifa {catid}")