from django.shortcuts import render

from django.http import request
from django.http import response
from django.http import HttpResponse
# Create your views here.

from .forms import DaylightHours #NEW
# from .models import User  #NEW





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

def p2_view_temp(request):
    return render(request , "p2.html")

def sr_view_temp(request):
    
    if request == "POST":
        fm = DaylightHours(request.POST)
        if fm.is_valid():
            dt = fm.data["date"]
            ltn = fm["latitude_south"]
            print(dt)
            print(ltn)
    else:
        fm = DaylightHours()
            
    return render(request , "srookie.html" , {'form':fm})






def result_view_temp(request):
    dt = request.POST["date"]
    print(dt)
    context = {}
    context["date"] = dt
    print(context)
    
    
    
    
    # return HttpResponse(f"The date is {dt}")
    return render(request , "result.html" , context)


