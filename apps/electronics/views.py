""" Views Electronics"""
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseServerError


from apps.core.models import ImageBase
from .forms import ElectronicForm
from .models import Electronic, ElectronicCategory


def electronic_add(request):
    """ Vista para electrónicos. """
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = ElectronicForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                images = request.FILES.getlist('images')
                print(data)
                category_id = request.POST.get('category_id')
                print("Categoría seleccionada:", category_id)

                new_electronic = Electronic.objects.create(
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
                    ImageBase.objects.create(image=image, product=new_electronic)

                messages.success(
                    request, '¡Producto de Electrónica agregado!'
                )

                return redirect(reverse('core:inicio'))

            else:
                print(request.FILES)
                print("Formulario no valido")
                print(form.errors)
                return HttpResponseServerError("Formulario no válido. Por favor, revise los datos.")

        else:
            form = ElectronicForm()

            context = {
                'categories': ElectronicCategory.objects.all(),
                'form': form,
            }

            return render(request, 'electronics/electronic_form.html', context)

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def electronics_list(request, id):

    category_instane = ElectronicCategory.objects.get(id=id)
    electronic_filter = Electronic.objects.filter(category=category_instane).order_by('-id')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(electronic_filter, 5)
        publications = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity': publications,
        'paginator': paginator
    }

    return render(request, 'electronics/list.html', context)


def edit_electronic(request, id):

    if request.user.is_authenticated:

        my_electronic = Electronic.objects.get(id=id)

        if request.method == 'POST':
            form = ElectronicForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data

                category_id = request.POST.get('category_id')
                category = ElectronicCategory.objects.get(id=category_id)

                my_electronic.title = data['title']
                my_electronic.price = data['price']
                my_electronic.location = data['location']
                my_electronic.phone_number1 = data['phone1']
                my_electronic.phone_number2 = data['phone2']
                my_electronic.email = data['email']
                my_electronic.description = data['description']
                my_electronic.category = category

                my_electronic.save()

                messages.success(request, 'Oferta de Electrónica editada')
                return redirect(reverse('core:inicio'))

            else:

                print("Formulario no valido")
                print(form.errors)
                return redirect(reverse('core:inicio'))

        else:

            data = {
                'title': my_electronic.title,
                'price': my_electronic.price,
                'location': my_electronic.location,
                'phone1': my_electronic.phone_number1,
                'phone2': my_electronic. phone_number2,
                'email': my_electronic.email,
                'description': my_electronic.description,
            }

            form = ElectronicForm(initial=data)

            return render(request, 'electronics/edit.html',
                          {'form': form,
                           'my_electronic': my_electronic,
                           'categories': ElectronicCategory.objects.all()}
                          )

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def delete_electronic(request, id):

    if request.user.is_authenticated:

        print(f'Electrónico con id: "{id}" eliminado')

        to_delete = Electronic.objects.get(id=id)
        to_delete.delete()

        messages.warning(request, 'Oferta de Electrónica eliminado!')

    else:
        print('WARNING')
        messages.error(request, 'Usuario no autentinca')

    return redirect(reverse('core:inicio'))
