from django.shortcuts import render
from .models import PageVisit

def HomeView(request):
    visitsCounter= PageVisit.objects.all()
    visits= PageVisit.objects.filter(path=request.path);
    myTitle= "Home Page of our app"
    PageVisit.objects.create(path= request.path)
    return render(request,template_name="index.html",context={'title':myTitle,'visitCounter':visits.count(),'totalVisits':visitsCounter.count()})
    