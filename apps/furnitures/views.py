""" Views Furniture. """
from django.shortcuts import redirect, render
from django.urls import reverse

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

    print(id)
    
    return render(request, 'furnitures/list.html')
