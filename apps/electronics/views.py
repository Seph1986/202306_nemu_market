""" Vistas Electronics"""
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Electronic, ElectronicCategory
from .forms import ElectronicForm

# Create your views here.
def electronic_add(request):
    """ Vista para electrónicos. """
    if request.method == 'POST':
        form = ElectronicForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # Obtiene los datos válidos del formulario
            images = request.FILES.getlist('images')
            print(data)
            # Crea un objeto Motor utilizando los datos válidos
            new_electronic = Electronic.objects.create(
                title=data['title'],
                description=data['description'],
                location=data['location'],
                price=data['price'],
            )

            return redirect(reverse('inicio'))

    else:
        form = ElectronicForm()

    context = {
        'categories': ElectronicCategory.objects.all(),
        'form': form,
    }

    return render(request, 'electronics/electronic_form.html', context)
