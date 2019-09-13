from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def home(request):
    return render(request, 'home.html')
 
def show(request):
    return render(request, 'show.html')
 
def new(request):
    return render(request, 'new.html')
 
def edit(request):
    return render(request, 'edit.html')
 
# def delete(request):
#     return HttpResponse('<h1>Herro Edit /ᐠ｡‸｡ᐟ\ﾉ</h1>')
 
# def login(request):
#     return HttpResponse('<h1>Herro Login /ᐠ｡‸｡ᐟ\ﾉ</h1>')