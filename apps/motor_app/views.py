""" Views Motors. """
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages


from .models import MotorCategory, Motor
from .forms import MotorForm


# Create your views here.
def motor_add(request):
    """ Vista para motorizados. """
    if request.method == 'POST':
        form = MotorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # images = request.FILES.getlist('images')
            category_id = request.POST.get('category_id')
            print("Categoría seleccionada:", category_id)

            # Crea un objeto Motor utilizando los datos válidos
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
                # images=images,
            )

            messages.success(
                request, 'Oferta de Motor agregado!'
            )

            return redirect(reverse('inicio'))

        else:
            print("Formulario no valido")
            print(form.errors)

    else:
        form = MotorForm()

    context = {
        'categories': MotorCategory.objects.all(),
        'form': form,
    }

    return render(request, 'motor_app/motor_form.html', context)


def motor_app_list(request, id):

    category_instane = MotorCategory.objects.get(id=id)
    motor_filter = Motor.objects.filter(category=category_instane)

    context = {
        'motors': motor_filter
    }

    return render(request, 'motor_app/list.html', context)


def delete_motor_app(request, id):

    print(f'Motor con id: "{id}" eliminado')

    to_delete = Motor.objects.get(id=id)
    to_delete.delete()

    messages.warning(
                request, 'Oferta de Motor eliminado!'
            )

    return redirect(reverse('inicio'))