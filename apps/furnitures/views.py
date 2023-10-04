""" Vistas Furniture. """
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


            new_electronic = Furniture.objects.create(
                name=data['name'],
                description=data['description'],
                location=data['location'],
                price=data['price'],
                category_id=category_id,
            )

            return redirect(reverse('furniture_add'))

    else:
        form = FurnitureForm()

    context = {
        'categories': FurnitureCategory.objects.all(),
        'form': form,
    }

    return render(request, 'furnitures/furniture_form.html', context)