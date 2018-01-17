from django.shortcuts import render
from django.http import HttpResponse
from webapp.models import *
# Create your views here.

def index(request):
    data=MCQ_Quiz.objects.all()
    data2=True_False.objects.all()
    data3=Txt_Question.objects.all()
    return render(request, 'index.html', {"data":data,"data2":data2,"data3":data3})
def store(request):
    User=request.GET.get("name")
    Contact=request.GET.get("contact")
    email=request.GET.get("email")
    a1=request.GET.get("1")
    a2=request.GET.get("2")
    a3=request.GET.get("3")
    a4=request.GET.get("4")
    a5=request.GET.get("5")
    a6=request.GET.get("6")
    a7=request.GET.get("7")
    a8=request.GET.get("8")
    a9=request.GET.get("9")
    a10=request.GET.get("10")
    s=Results()
    s.user=User
    s.contact=Contact
    s.email=email
    s.a1=a1
    s.a2=a2
    s.a3=a3
    s.a4=a4
    s.a5=a5
    s.a6=a6
    s.a7=a7
    s.a8=a8
    s.a9=a9
    s.a10=a10
    s.save()
    return render(request,'save.html')

def about(request):
    return render(request,'about.html')

