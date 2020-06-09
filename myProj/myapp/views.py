from django.shortcuts import render

# Create your views here.
from .models import Teach

def View(request):
    if request.method == 'POST':
        title1=request.POST.get("title")
        message1=request.POST.get("description")
        timer=request.POST.get('timer')


        e=Teach(Title=title1,description=message1,time=timer)
        e.save()
        print(title1,message1,timer)

    return render(request, 'entry.html')




def EntryShow(request):
    all= Teach.objects.all()
    return render(request,"entryshow.html",{'bell':all})