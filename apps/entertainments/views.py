""" Views Entertainments. """
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import EntertainmentForm
from .models import Entertainment, EntertainmentCategory


# Create your views here.
def entertainment_add(request):
    """ Vista para electrónicos. """
    if request.method == 'POST':
        form = EntertainmentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # images = request.FILES.getlist('images')
            category_id = request.POST.get('category_id')
            print("Categoría seleccionada:", category_id)

            new_entertainment = Entertainment.objects.create(
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

            return redirect(reverse('inicio'))

        else:
            print("Formulario no valido")
            print(form.errors)

    else:
        form = EntertainmentForm()

    context = {
        'categories': EntertainmentCategory.objects.all(),
        'form': form,
    }

    return render(request, 'entertainments/entertainments_form.html', context)


def entertainments_list(request, id):

    category_instane = EntertainmentCategory.objects.get(id=id)
    entertainment_filter = Entertainment.objects.filter(category=category_instane)

    context = {
        'electronics': entertainment_filter
    }

    return render(request, 'entertainments/list.html', context)