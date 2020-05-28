from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GeolocationData
from .form import GeoDataForm

# Create your views here.
def index(request):
    return render(request, 'geolocationapp/index.html')

def getGeolocationData(request):
    geodata=GeolocationData.objects.all()
    return render(request, 'geolocationapp/geodata.html', {'geodata':geodata})

@login_required()
def newGeolocationData(request):
    form=GeoDataForm
    if request.method=="POST":
        form=GeoDataForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=GeoDataForm()
        else:
            form=GeoDataForm()
    return render(request, 'geolocationapp/newgeodata.html', {'form':form})

def loginmessage(request):
    return render(request, 'geolocationapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'geolocationapp/logoutmessage.html')