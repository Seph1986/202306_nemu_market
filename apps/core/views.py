from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
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

    print(request.POST['search'])

    return render(request, 'nemu/search_results.html')