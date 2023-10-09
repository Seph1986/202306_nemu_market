""" Views Furniture. """
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages


from .models import Furniture, FurnitureCategory
from .forms import FurnitureForm

# Create your views here.


def furniture_add(request):
    """ Vista para electrónicos. """
    if request.method == 'POST':
        form = FurnitureForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # images = request.FILES.getlist('images')
            category_id = request.POST.get('category_id')
            print("Categoría seleccionada:", category_id)

            new_forniture = Furniture.objects.create(
                title=data['title'],
                category_id=category_id,
                price=data['price'],
                location=data['location'],
                phone_number1=data['phone1'],
                phone_number2=data['phone2'],
                email=data['email'],
                description=data['description'],
                user=request.user,
            )

            messages.success(
                request, 'Oferta de Mobiliario agregado!'
            )

            return redirect(reverse('inicio'))

        else:
            print("Formulario no valido")
            print(form.errors)

    else:
        form = FurnitureForm()

    context = {
        'categories': FurnitureCategory.objects.all(),
        'form': form,
    }

    return render(request, 'furnitures/furniture_form.html', context)


def furnitures_list(request, id):

    category_instane = FurnitureCategory.objects.get(id=id)
    furniture_filter = Furniture.objects.filter(category=category_instane)

    context = {
        'furnitures': furniture_filter
    }

    return render(request, 'furnitures/list.html', context)


def delete_furniture(request, id):

    print(f'Mobiliario con id: "{id}" eliminado')

    to_delete = Furniture.objects.get(id=id)
    to_delete.delete()

    messages.warning(
                request, 'Oferta de Mobiliario eliminado!'
            )

    return redirect(reverse('inicio'))
