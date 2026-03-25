from django.shortcuts import render
from app.models import *

# Create your views here.
def display_countries(request):
    QSLCO=Country.objects.all()
    d={'QSLCO':QSLCO}
    return render(request,'displaycountry.html',d)

def display_capitals(request):
    QSLCAP=Capital.objects.all()
    d={'QSLCAP':QSLCAP}
    return render(request,'displaycapital.html',d)