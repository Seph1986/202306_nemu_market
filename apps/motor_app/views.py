""" Views Motors. """
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseServerError

from apps.core.models import ImageBase
from .models import MotorCategory, Motor
from .forms import MotorForm


# Create your views here.
def motor_add(request):
    """ Vista para motorizados. """
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MotorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                images = request.FILES.getlist('images')
                category_id = request.POST.get('category_id')
                print("Categoría seleccionada:", category_id)

                new_motor = Motor.objects.create(
                    title=data['title'],
                    price=data['price'],
                    location=data['location'],
                    brand=data['brand'],
                    model=data['model'],
                    fuel=data['fuel'],
                    transmission=data['transmission'],
                    year=int(data['year']),
                    color=data['color'],
                    category_id=category_id,
                    email=data['email'],
                    phone_number1=data['phone1'],
                    phone_number2=data['phone2'],
                    description=data['description'],
                    user=request.user,
                )

                images = request.FILES.getlist('images')
                for image in images:
                    ImageBase.objects.create(image=image, product=new_motor)

                messages.success(
                    request, 'Oferta de Motor agregado!'
                )

                return redirect(reverse('core:inicio'))

            else:
                print(request.FILES)
                print("Formulario no valido")
                print(form.errors)
                return HttpResponseServerError("Formulario no válido. Por favor, revise los datos.")

        else:
            form = MotorForm()

        context = {
            'categories': MotorCategory.objects.all(),
            'form': form,
        }

        return render(request, 'motor_app/motor_form.html', context)

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def motor_app_list(request, id):

    category_instane = MotorCategory.objects.get(id=id)
    motor_filter = Motor.objects.filter(category=category_instane).order_by('-id')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(motor_filter, 5)
        publications = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity': publications,
        'paginator': paginator
    }

    return render(request, 'motor_app/list.html', context)


def edit_motor_app(request, id):

    if request.user.is_authenticated:

        my_motor = Motor.objects.get(id=id)

        if request.method == 'POST':
            form = MotorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data

                category_id = request.POST.get('category_id')
                category = MotorCategory.objects.get(id=category_id)

                #Motor data
                my_motor.brand = data['brand']
                my_motor.model = data['model']
                my_motor.fuel = data['fuel']
                my_motor.transmission = data['transmission']
                my_motor.year = data['year']
                my_motor.color = data['color']

                #Base data
                my_motor.title = data['title']
                my_motor.price = data['price']
                my_motor.location = data['location']
                my_motor.phone_number1 = data['phone1']
                my_motor.phone_number2 = data['phone2']
                my_motor.email = data['email']
                my_motor.description = data['description']
                my_motor.category = category

                my_motor.save()

                messages.success(request, 'Oferta de Motorizado editada')
                return redirect(reverse('core:inicio'))

            else:

                print("Formulario no valido")
                print(form.errors)
                return redirect(reverse('core:inicio'))

        else:

            data = {
                #Motor
                'brand': my_motor.brand,
                'model': my_motor.title,
                'fuel': my_motor.fuel,
                'transmission': my_motor.transmission,
                'year': my_motor.year,
                'color': my_motor.color,
                #Base
                'title': my_motor.title,
                'price': my_motor.price,
                'location': my_motor.location,
                'phone1': my_motor.phone_number1,
                'phone2': my_motor. phone_number2,
                'email': my_motor.email,
                'description': my_motor.description,
            }

            form = MotorForm(initial=data)

            return render(request, 'motor_app/edit.html',
                          {'form': form,
                           'my_motor': my_motor,
                           'categories': MotorCategory.objects.all()}
                          )

    else:
        messages.error(request, '¡Usuario no autenticado!')
        return redirect(reverse('core:inicio'))


def delete_motor_app(request, id):

    print(f'Motor con id: "{id}" eliminado')

    to_delete = Motor.objects.get(id=id)
    to_delete.delete()

    messages.warning(
                request, 'Oferta de Motor eliminado!'
            )

    return redirect(reverse('core:inicio'))