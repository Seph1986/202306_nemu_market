""" Views Users. """
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from apps.electronics.models import Electronic
from apps.entertainments.models import Entertainment
from apps.furnitures.models import Furniture
from apps.motor_app.models import Motor
from .forms import RegisterUserForm, ChangeProfilePictureForm
from .models import Profile


def login_user(request):
    """ Vista para inicio de sesión. """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('core:inicio')
        else:
            messages.error(
                request, "Hubo un error al iniciar sesión, inténtalo de nuevo.")
            return redirect('users:login')
    else:
        return render(request, 'authenticate/login.html', {})


@login_required
def logout_user(request):
    """ Vista para cierre de sesión. """
    logout(request)
    messages.success(request, ("El cierre de sesión se realizó exitosamente."))
    return redirect('core:inicio')


def register_user(request):
    """ Vista para registro de usuario. """
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile, created = Profile.objects.get_or_create(user=user)
            if created or not profile.profile_img:
                profile.profile_img = 'images/user_default_icon.png'
                profile.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("El registro se realizó exitosamente."))
            return redirect('core:inicio')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })


@login_required
def user_profile(request, pk):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user_id=pk)
        is_owner = request.user == profile.user

        # Combina todas las publicaciones del usuario en todas las categorías
        all_publications = (
            list(Electronic.objects.filter(user=profile.user)) +
            list(Entertainment.objects.filter(user=profile.user)) +
            list(Furniture.objects.filter(user=profile.user)) +
            list(Motor.objects.filter(user=profile.user))
        )

        # Puedes agregar otras categorías de publicaciones aquí

        # Ordena las publicaciones por fecha (u otro criterio relevante)
        all_publications.sort(key=lambda x: x.created_at, reverse=True)

        if request.method == 'POST' and is_owner:
            form = ChangeProfilePictureForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'La foto de perfil se ha actualizado correctamente.')

        form = ChangeProfilePictureForm(instance=profile) if is_owner else None

        return render(request, "authenticate/user_profile.html", {
            "profile": profile,
            "form": form,
            "is_owner": is_owner,
            "all_publications": all_publications,
        })
    else:
        messages.error(request, ("Debes iniciar sesión para ver esta página."))
        return redirect('core:inicio')


@login_required
def change_profile_picture(request):
    if request.method == 'POST':
        form = ChangeProfilePictureForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'La foto de perfil se ha actualizado correctamente.')
            return redirect('user_profile', pk=request.user.pk)
    else:
        form = ChangeProfilePictureForm(instance=request.user.profile)
    return render(request, 'authenticate/user_profile.html', {'form': form})


