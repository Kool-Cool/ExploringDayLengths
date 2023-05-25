from django.shortcuts import render

from django.http import request
from django.http import response
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return HttpResponse('''This is Home Page .
                            Welcome !!
                            Hemlo World !!!
                        ''')
    
def home_view_temp(request):
    return render(request,"home.html")


def about_view_temp(request):
    return render(request ,"about.html")

def coffee_view_temp(request):
    return render(request , "coffee.html")