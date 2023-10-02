""" User Forms. """
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    """ Formulario de registro para usuario."""
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class':'form-control'}),
    )
    first_name = forms.CharField(
        max_length=50,
        label="Nombre",
        widget=forms.TextInput(attrs={'class':'form-control'}),
        )
    last_name = forms.CharField(
        max_length=50,
        label="Apellido",
        widget=forms.TextInput(attrs={'class':'form-control'}),
        )

    class Meta:
        """ Metadatos para formulario de registro. """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username': 'Usuario',
            'password1': 'Contraseña',
            'password2': 'Contraseña (confirmación)',
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class LoginForm(AuthenticationForm):
    """ Formulario de ingreso par usuario. """
    class Meta:
        """ Metadatos para formulario de ingreso. """
        model = User
        fields = ['username', 'password']
