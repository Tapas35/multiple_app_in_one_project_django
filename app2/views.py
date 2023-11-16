from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def havingjob(request):
    return render (request,'temp2.html')

def func1 (request):
    return HttpResponse('<h1> app2 HttpResponse</h1>')