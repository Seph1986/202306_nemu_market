""" Views Furniture. """
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseServerError

from apps.core.models import ImageBase
from .models import Furniture, FurnitureCategory
from .forms import FurnitureForm

# Create your views here.


def furniture_add(request):
    """ Vista para electrónicos. """
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FurnitureForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                images = request.FILES.getlist('images')
                category_id = request.POST.get('category_id')
                print("Categoría seleccionada:", category_id)

                new_furniture = Furniture.objects.create(
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

                images = request.FILES.getlist('images')
                for image in images:
                    ImageBase.objects.create(image=image, product=new_furniture)

                messages.success(
                    request, 'Oferta de Mobiliario agregado!'
                )

                return redirect(reverse('core:inicio'))

            else:
                print(request.FILES)
                print("Formulario no valido")
                print(form.errors)
                return HttpResponseServerError("Formulario no válido. Por favor, revise los datos.")

        else:
            form = FurnitureForm()

        context = {
            'categories': FurnitureCategory.objects.all(),
            'form': form,
        }

        return render(request, 'furnitures/furniture_form.html', context)

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def furnitures_list(request, id):

    category_instane = FurnitureCategory.objects.get(id=id)
    furniture_filter = Furniture.objects.filter(category=category_instane).order_by('-id')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(furniture_filter, 5)
        publications = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity': publications,
        'paginator': paginator
    }

    return render(request, 'furnitures/list.html', context)


def edit_furniture(request, id):

    if request.user.is_authenticated:

        my_furniture = Furniture.objects.get(id=id)

        if request.method == 'POST':
            form = FurnitureForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data

                category_id = request.POST.get('category_id')
                category = FurnitureCategory.objects.get(id=category_id)

                my_furniture.title = data['title']
                my_furniture.price = data['price']
                my_furniture.location = data['location']
                my_furniture.phone_number1 = data['phone1']
                my_furniture.phone_number2 = data['phone2']
                my_furniture.email = data['email']
                my_furniture.description = data['description']
                my_furniture.category = category

                my_furniture.save()

                messages.success(request, 'Oferta de Mobiliario editada')
                return redirect(reverse('core:inicio'))

            else:

                print("Formulario no valido")
                print(form.errors)
                return redirect(reverse('core:inicio'))

        else:

            data = {
                'title': my_furniture.title,
                'price': my_furniture.price,
                'location': my_furniture.location,
                'phone1': my_furniture.phone_number1,
                'phone2': my_furniture. phone_number2,
                'email': my_furniture.email,
                'description': my_furniture.description,
            }

            form = FurnitureForm(initial=data)

            return render(request, 'furnitures/edit.html',
                        {'form': form,
                        'my_furniture': my_furniture,
                        'categories': FurnitureCategory.objects.all()}
                        )

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def delete_furniture(request, id):

    print(f'Mobiliario con id: "{id}" eliminado')

    to_delete = Furniture.objects.get(id=id)
    to_delete.delete()

    messages.warning(
                request, 'Oferta de Mobiliario eliminado!'
            )

    return redirect(reverse('core:inicio'))
