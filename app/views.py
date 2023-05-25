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