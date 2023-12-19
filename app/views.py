from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
def display_topics(request):
    QLTO=Topic.objects.all()
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name')) 
     
      

    d={'QLTO':QLTO}




    return render(request,'display_topics.html',d)


def webpage(request):
    WLTO=Webpage.objects.all()
    WLTO=Webpage.objects.all().order_by('topic_name')
    WLTO=Webpage.objects.all().order_by('-topic_name')
    WLTO=Webpage.objects.all().order_by('name')
    WLTO=Webpage.objects.all().order_by('-name')
    WLTO=Webpage.objects.all().order_by(Length('name'))
    WLTO=Webpage.objects.all().order_by(Length('name').desc())
    WLTO=Webpage.objects.filter(topic_name='cricketer')

    d={'WLTO':WLTO}
    return render(request,'webpage.html',d)


def insert_topic(request):
    tn=input()
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('Topic is inserted')

def insert_webpage(request):
    tn=input('enter the topic name')
    n=input('enter the name')
    u=input('enter the url')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    return HttpResponse('webpage is created')

def display_acess(request):
    ALTO=AccessRecord.objects.all()
    ALTO=AccessRecord.objects.filter(date__year__lt='2022')
    ALTO=AccessRecord.objects.filter(date__year__gt='2022')
    ALTO=AccessRecord.objects.filter(date__year__lte='2022')
    ALTO=AccessRecord.objects.filter(date__year__gte='2022')
    ALTO=AccessRecord.objects.filter(date__month__lte='2022')
    ALTO=AccessRecord.objects.filter(date__year__lte='2022')
    ALTO=AccessRecord.objects.filter(date__year__gte='2022')
    ALTO=AccessRecord.objects.filter(author__contains='na')
    
    d={'ALTO':ALTO}
    return render(request,'display_acess.html',d)