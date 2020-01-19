from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.



def home(request):
        return render(request, "index.html")

def home_redirect(request):
        return redirect('index.html')

