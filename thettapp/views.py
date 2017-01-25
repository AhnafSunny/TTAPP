from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):

    return render(request,'thettapp/index.html')

def playerCreate(request):
    return HttpResponse('<h1>player create</h1>')

def teamCreate(request):
    return HttpResponse('<h1>team create</h1>')

def matchCreate(request):
    return HttpResponse('<h1>match create</h1>')