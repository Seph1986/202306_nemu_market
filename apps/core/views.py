from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from apps.electronics.models import ElectronicCategory
from apps.entertainments.models import EntertainmentCategory
from apps.furnitures.models import FurnitureCategory
from apps.motor_app.models import MotorCategory


# Create your views here.
def index(request):
    # Agregar un mensaje de éxito
    messages.success(request, "¡Disfruta del sitio web!")

    context = {
        'electronics': ElectronicCategory.objects.all(),
        'entertainments': ElectronicCategory.objects.all(),
        'furnitures': FurnitureCategory.objects.all(),
        'motors': MotorCategory.objects.all()
    }

    return render(request, 'landing/index.html', context)
