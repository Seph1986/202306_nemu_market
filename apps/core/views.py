from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from apps.core.models import BaseClass
from apps.electronics.models import ElectronicCategory
from apps.entertainments.models import EntertainmentCategory
from apps.furnitures.models import FurnitureCategory
from apps.motor_app.models import MotorCategory


# Create your views here.
def index(request):
    
    context = {
        'electronics': ElectronicCategory.objects.all(),
        'entertainments': EntertainmentCategory.objects.all(),
        'furnitures': FurnitureCategory.objects.all(),
        'motors': MotorCategory.objects.all()
    }

    return render(request, 'nemu/index.html', context)


def search_results(request):
    
    if request.method == 'POST':

        searched = request.POST['search']
        print(searched)

        found = BaseClass.objects.filter(title__contains= searched)

        context = {
            'searched': searched,
            'found': found
        }

        return render(request, 'nemu/search_results.html', context) 


    else: 
        
        #FALTA AGREGAR PROTECCIÓN CONTRA REVERSE

        return render(request, 'nemu/search_results.html')
