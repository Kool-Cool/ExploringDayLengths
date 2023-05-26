from django.shortcuts import render

from django.http import request
from django.http import response
from django.http import HttpResponse
# Create your views here.

from .forms import DaylightHours #NEW
# from .models import User  #NEW



from datetime import datetime
from math import sin , asin , cos , acos ,tan , atan , pi 

def day_lenght(L:float ,fun_date=1 , fun_month=1 , fun_year=2023 ):
    """  
    L:- lattitude in degrees
    
    """
    
    date1 = datetime(day=fun_date , month=fun_month,  year=fun_year)
    date2 = datetime(day= 1 ,month=1 ,year= fun_year)
    day_count = date1 - date2
    
    P = asin(0.39795*cos(0.2163108 + 2*atan(0.9671396*tan(0.00860*((day_count.days)-186)))))
    
    num = sin(0.8333*pi/180) + sin(L*pi/180)*sin(P)
    deno = cos(L*pi/180)*cos(P)
    
    D = 24 - (24/pi)*acos(num/deno)
    
    return D









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

def se_view_temp(request):
    if request == "POST":
        fm = DaylightHours(request.POST)
        if fm.is_valid():
            dt = fm.data["date"]
            ltn = fm["latitude_south"]
            print(dt)
            print(ltn)
    else:
        fm = DaylightHours()
            
    return render(request , "senthu.html" , {'form':fm})
    






def result_view_temp(request):
    dt = int(request.POST["date"])
    mt = int(request.POST["month"])
    yt = int(request.POST["year"])
    lt  = float(request.POST["latitude"])
    
    context = {}
    context["date"] = (dt)
    context["month"] = mt
    context["year"] = yt
    context["latitude"] = float(lt)
    
    
    context["result"] = day_lenght(lt , dt ,mt , yt)
    
    print(context)
    
    # return HttpResponse(f"The date is {dt}")
    return render(request , "result.html" , context)


from datetime import datetime
from math import sin , asin , cos , acos ,tan , atan , pi 

def day_lenght(L:float ,fun_date=1 , fun_month=1 , fun_year=2023 ):
    """  
    L:- lattitude in degrees
    
    """
    
    date1 = datetime(day=fun_date , month=fun_month,  year=fun_year)
    date2 = datetime(day= 1 ,month=1 ,year= fun_year)
    day_count = date1 - date2
    
    P = asin(0.39795*cos(0.2163108 + 2*atan(0.9671396*tan(0.00860*((day_count.days)-186)))))
    
    num = sin(0.8333*pi/180) + sin(L*pi/180)*sin(P)
    deno = cos(L*pi/180)*cos(P)
    
    D = 24 - (24/pi)*acos(num/deno)
    
    return D