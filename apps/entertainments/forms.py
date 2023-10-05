""" Forms Entertainments. """
from django import forms

class EntertainmentForm(forms.Form):
    """ Formularios para oferta de entretenimientos. """
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Título',
        max_length=255,
        min_length=1,
        required=True,
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Descripción',
        max_length=255,
        min_length=1,
        required=True,
    )

    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Ubicación',
        max_length=255,
        min_length=4,
        required=True,
    )

    price = forms.IntegerField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Precio',
        min_value=1,
        required=True,
        error_messages={
            'invalid': 'Por favor, ingrese un número válido para el precio.',
        }
    )

    phone1 = forms.IntegerField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Celular 1',
        min_value=1,
        required=True,
        error_messages={
            'invalid': 'Por favor, ingrese un número de contacto válido',
        }

    )

    phone2 = forms.IntegerField(
            widget=forms.TextInput(attrs={'class':'form-control'}),
            label='Celular 2',
            min_value=1,
        )

    email = forms.IntegerField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Email',
        min_value=1,
        error_messages={
            'invalid': 'Por favor, ingrese un email válido.',
        }

    )
