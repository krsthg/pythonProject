from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def join(request):
    return render(request, 'join.html')

def board(request):
    return render(request, 'board.html')

def write(request):
    return render(request, 'write.html')

def boardview(request):
    return render(request, 'boardview.html')

def intro(request):
    return render(request, 'intro.html')

def detail(request):
    return render(request, 'detail.html')