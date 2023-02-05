from django.shortcuts import render
from.models import tour,actor
# Create your views here.
def demo(request):
    obj=tour.objects.all()
    obv=actor.objects.all()
    return render(request,'index.html',{'result':obj,'resul':obv})

