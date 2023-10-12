""" Views Entertainments. """
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseServerError

from apps.core.models import ImageBase
from .forms import EntertainmentForm
from .models import Entertainment, EntertainmentCategory


def entertainment_add(request):
    """ Vista para electrónicos. """
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = EntertainmentForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                images = request.FILES.getlist('images')
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

                images = request.FILES.getlist('images')
                for image in images:
                    ImageBase.objects.create(image=image, product=new_entertainment)

                messages.success(
                    request, 'Oferta de Entretenimiento agregado!'
                )

                return redirect(reverse('core:inicio'))

            else:
                print(request.FILES)
                print("Formulario no valido")
                print(form.errors)
                return HttpResponseServerError("Formulario no válido. Por favor, revise los datos.")

        else:
            form = EntertainmentForm()

            context = {
                'categories': EntertainmentCategory.objects.all(),
                'form': form,
            }

            return render(request, 'entertainments/entertainments_form.html', context)

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))



def entertainments_list(request, id):

    category_instane = EntertainmentCategory.objects.get(id=id)
    entertainment_filter = Entertainment.objects.filter(category=category_instane).order_by('-id')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(entertainment_filter, 5)
        publications = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity': publications,
        'paginator': paginator
    }

    return render(request, 'entertainments/list.html', context)


def edit_entertainment(request, id):

    if request.user.is_authenticated:

        my_entertainment = Entertainment.objects.get(id=id)

        if request.method == 'POST':
            form = EntertainmentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data

                category_id = request.POST.get('category_id')
                category = EntertainmentCategory.objects.get(id=category_id)

                my_entertainment.title = data['title']
                my_entertainment.price = data['price']
                my_entertainment.location = data['location']
                my_entertainment.phone_number1 = data['phone1']
                my_entertainment.phone_number2 = data['phone2']
                my_entertainment.email = data['email']
                my_entertainment.description = data['description']
                my_entertainment.category = category

                my_entertainment.save()

                messages.success(request, 'Oferta de Entretenimiento editada')
                return redirect(reverse('core:inicio'))

            else:

                print("Formulario no valido")
                print(form.errors)
                return redirect(reverse('core:inicio'))

        else:

            data = {
                'title': my_entertainment.title,
                'price': my_entertainment.price,
                'location': my_entertainment.location,
                'phone1': my_entertainment.phone_number1,
                'phone2': my_entertainment. phone_number2,
                'email': my_entertainment.email,
                'description': my_entertainment.description,
            }

            form = EntertainmentForm(initial=data)

            return render(request, 'entertainments/edit.html',
                          {'form': form,
                           'my_entertainment': my_entertainment,
                           'categories': EntertainmentCategory.objects.all()}
                          )

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def delete_entertainment(request, id):

    print(f'Entretenimiento con id: "{id}" eliminado')

    to_delete = Entertainment.objects.get(id=id)
    to_delete.delete()

    messages.warning(
                request, 'Oferta de Entretenimiento eliminado!'
            )

    return redirect(reverse('core:inicio'))
