from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('inicio')
        else:
            messages.error(request, "Hubo un error al iniciar sesión, inténtalo de nuevo.")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})




def logout_user(request):
    """ Vista para cierre de sesión. """
    logout(request)
    messages.success(request, ("El cierre de sesión se realizó exitosamente."))
    return redirect('inicio')

def register_user(request):
    """ Vista para registro de usuario. """
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("El registro se realizó exitosamente."))
            return redirect('inicio')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })
