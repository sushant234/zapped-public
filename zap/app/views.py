from django.shortcuts import render
from app.models import *
# Create your views here.

def index(request):
    context = {}
    context['employee'] = employee.objects.all()
    context['client'] = client.objects.all()
    context['homepage'] = homepage.objects.all()
    # context['feedback'] = feedback.objects.all()
    if 'butt4' in request.POST:
        name = request.POST['name']
        print(name)
        email = request.POST['email']
        print(email)
        message = request.POST['message']
        print(message)
        dd = feedback(name=name,email=email,message=message)
        dd.save()
    return render(request,'index.html',context)

def blogg(request):
    context = {}
    context['blog'] = blog.objects.all() 
    return render(request,'blog.html',context)

def singleblog(request,value):
    context={}
    context['sblog'] = blog.objects.get(id=value)
    return render(request,'singleblog.html',context)

def catalogue(request):
    return render(request,'catalogue.html')

def ml(request):
    context = {}
    context['mldesc'] = mldesc.objects.all()
    context['mldescbox'] = mldescbox.objects.all()
    return render(request,'maclea.html',context)

def ds(request):
    context = {}
    context['dsdesc'] = dsdesc.objects.all()
    context['dsdescbox'] = dsdescbox.objects.all()
    return render(request,'digseo.html',context)

def wd(request):
    context={}
    context['wddesc'] = wddesc.objects.all()
    context['wddescbox'] = wddescbox.objects.all()
    return render(request,'webdev.html',context)

def ad(request):
    context={}
    context['addesc'] = addesc.objects.all()
    context['addescbox'] = addescbox.objects.all()
    return render(request,'anddev.html',context)