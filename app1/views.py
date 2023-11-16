from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def temp1(request):
    return render (request,'temp1.html')

def func (request):
    return HttpResponse('<h1> this is a HttpResponse</h1>')