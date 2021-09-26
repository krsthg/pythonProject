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

def word(request):
    return render(request, 'word.html')

def Idiomatic(request):
    return render(request, 'Idiomatic.html')

def Proverb(request):
    return render(request, 'Proverb.html')

def Abbreviation(request):
    return render(request, 'Abbreviation.html')

def Idiom(request):
    return render(request, 'Idiom.html')

def A2(request):
    return render(request, 'A2.html')

def I2(request):
    return render(request, 'I2.html')

def Id2(request):
    return render(request, 'Id2.html')

def Id3(request):
    return render(request, 'Id3.html')

def P2(request):
    return render(request, 'P2.html')

def W2(request):
    return render(request, 'W2.html')

def W3(request):
    return render(request, 'W3.html')

def W4(request):
    return render(request, 'W4.html')

def W5(request):
    return render(request, 'W5.html')

def W6(request):
    return render(request, 'W6.html')

def W7(request):
    return render(request, 'W7.html')

