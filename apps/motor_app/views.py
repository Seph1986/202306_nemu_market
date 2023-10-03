from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Category, Motor
from .forms import MotorForm


# Create your views here.
def motor_add(request):
    if request.method == 'POST':
        form = MotorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # Obtiene los datos válidos del formulario
            # images = request.FILES.getlist('images')
            category = Category.objects.get(id=data['category_id'])
            
            # Crea un objeto Motor utilizando los datos válidos
            new_motor = Motor.objects.create(
                brand=data['brand'],
                model=data['model'],
                fuel=data['fuel'],
                transmission=data['transmission'],
                year=int(data['year']),
                color=data['color'],
                location=data['location'],
                price=data['price'],
                # images=images,
                category=category
            )

            return redirect(reverse('motor_add'))

    else:
        form = MotorForm()

    context = {
        'categories': Category.objects.all(),
        'form': form,
    }

    return render(request, 'motor_app/motor_form.html', context)
