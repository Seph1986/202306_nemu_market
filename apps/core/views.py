from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from apps.core.models import BaseClass
from apps.electronics.models import ElectronicCategory
from apps.entertainments.models import EntertainmentCategory
from apps.furnitures.models import FurnitureCategory
from apps.motor_app.models import MotorCategory
from apps.users.models import Profile


# Create your views here.
def index(request):
    """Vista para inicio"""

    context = {
        'electronics': ElectronicCategory.objects.all(),
        'entertainments': EntertainmentCategory.objects.all(),
        'furnitures': FurnitureCategory.objects.all(),
        'motors': MotorCategory.objects.all()
    }

    return render(request, 'nemu/index.html', context)


def search_results(request):
    """Vista para resultados del search. """
    if request.method == 'POST':

        searched = request.POST['search']
        found = BaseClass.objects.filter(title__contains= searched)

        context = {
            'searched': searched,
            'found': found
        }

        return render(request, 'nemu/search_results.html', context)


    else:

        #FALTA AGREGAR PROTECCIÓN REENVIO DE FORMULARIO

        return render(request, 'nemu/search_results.html')
    

def favorite_control(request, id):

    if request.user.is_authenticated:

        my_user = request.user
        
        user =Profile.objects.get(id=my_user.id)

        for fav in user.favorites.all():
            print(fav.title)
        
        publication = BaseClass.objects.get(id=id)

        if not user.favorites.filter(id=publication.id).exists():
            user.favorites.add(publication)
            messages.success(request,f'Agregado a favoritos {publication.title}')
        else:
            user.favorites.remove(publication)
            messages.warning(request,f'Removido de favoritos {publication.title}')
            

        return redirect(reverse('core:inicio'))

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def show_detail(request, id):

    if request.user.is_authenticated:
        
        return render(request, 'nemu/show_detail.html')

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))