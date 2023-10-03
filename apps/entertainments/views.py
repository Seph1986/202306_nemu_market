from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import EntertainmentForm
from .models import Entertainment, EntertainmentCategory


# Create your views here.
def entertainment_form(request):
    
    if request.method == 'POST':
        form =  EntertainmentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # category = EntertainmentCategory.objects.get(id=data['category_id'])
            
            print(data, form)

            # Entertainment.objects.create(
            #     name = data['name'],
            #     description = data['description'],
            #     price = data['price'],
            #     location = data['location'],
            #     category = category
            # )

        return redirect(reverse('entertainment_form'))

    context = {
        'categories': EntertainmentCategory.objects.all(),
        'form': EntertainmentForm()
    }
    return render(request, 'entertainments_form.html', context)
