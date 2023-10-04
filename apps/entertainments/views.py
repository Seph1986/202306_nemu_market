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
            images = request.FILES.getlist('images')


            new_electronic = Entertainment.objects.create(
                title=data['title'],
                description=data['description'],
                location=data['location'],
                price=data['price'],
            )

            return redirect(reverse('entertainment_add'))

    else:
        form = EntertainmentForm()

    context = {
        'categories': EntertainmentCategory.objects.all(),
        'form': form,
    }

    return render(request, 'entertainments/entertainments_form.html', context)
