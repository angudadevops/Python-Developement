from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
'''
def index(request):
 return HttpResponse('<h1>I am the root of Tracker App<h1>')
'''
def index(request):
 return render(request, 'index.html')