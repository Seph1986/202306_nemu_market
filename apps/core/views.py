from django.conf import settings
from django.contrib import messages
from django.shortcuts import render


# Create your views here.
def index(request):
    # Agregar un mensaje de éxito
    messages.success(request, "¡Bienvenido a mi sitio web!")

    return render(request, 'landing/index.html')
