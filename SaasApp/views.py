from django.shortcuts import render
from .models import PageVisit

def HomeView(request):
    return AboutView(request)

def AboutView(request):
    totalVists= PageVisit.objects.all()
    visits= PageVisit.objects.filter(path=request.path);
    myTitle= "Home Page of our app"
    PageVisit.objects.create(path= request.path)
    
    context={
        'title':myTitle,
        'pathVisits':visits.count(),
        'totalVisits':totalVists.count(),
        'percentageVisits': totalVists.count()/visits.count()
    }
    
    return render(request,"index.html",context)