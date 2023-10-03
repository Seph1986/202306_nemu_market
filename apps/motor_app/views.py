from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Category, Motor


# Create your views here.
def motor_add(request):

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        category = Category.objects.get(id=data['category_id'])
        print(data, images)

        # new_motor = Motor.objects.create(
        #     brand= data['brand'],
        #     model= data['model'],
        #     fuel= data['fuel'],
        #     transmission= data['transmission'],
        #     year= int(data['year']),
        #     color= data['color'],
        #     location= data['location'],
        #     price= data['price'],
        #     images= images,
        #     category= category
        # )
        
        return redirect(reverse('motor_add'))

    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'motor_app/form.html', context)
