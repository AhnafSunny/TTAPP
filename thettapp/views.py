from django.shortcuts import render,HttpResponse

# Create your views here.

from . models import player

def index(request):

    return render(request,'thettapp/index.html')

def playerCreate(request):
    return render(request,'thettapp/playercreate.html')

def teamCreate(request):
    return HttpResponse('<h1>team create</h1>')

def matchCreate(request):
    return HttpResponse('<h1>match create</h1>')

def playerAdd(request):
    s = request.POST['name']
    if(s == ""):
        return HttpResponse('<h1>Empty String</h1>')
    else:
        p1 = player()
        p1.name = s
        p1.save()
        return render(request,'thettapp/playerbrowse.html')

