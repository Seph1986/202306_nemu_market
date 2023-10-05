""" Views Electronics"""
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ElectronicForm
from .models import Electronic, ElectronicCategory

# Create your views here.


def electronic_add(request):
    """ Vista para electrónicos. """
    if request.method == 'POST':
        form = ElectronicForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # Obtiene los datos válidos del formulario
            images = request.FILES.getlist('images')
            print(data)
            # images = request.FILES.getlist('images')
            category_id = request.POST.get('category_id')
            print("Categoría seleccionada:", category_id)

            # Crea un objeto Motor utilizando los datos válidos
            new_electronic = Electronic.objects.create(
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
        form = ElectronicForm()
        print(ElectronicForm.errors)

    context = {
        'categories': ElectronicCategory.objects.all(),
        'form': form,
    }

    return render(request, 'electronics/electronic_form.html', context)
