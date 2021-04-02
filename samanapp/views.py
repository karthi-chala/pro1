from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def insert(request):
    return  HttpResponse('<h1>paditha udan kilith vidaumm kilitha undan koteyei nasakum </h1>')
    
def sam(request):
    return render(request,'samplee.html')