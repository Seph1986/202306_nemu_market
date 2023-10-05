""" Forms Motors. """
from datetime import date

from django import forms


class MotorForm(forms.Form):
    """ Formularios para oferta de mobliliarios. """
    FUEL_CHOICES = [
        ('gas','Nafta'),
        ('diesel', 'Diesel'),
        ('alcohol', 'Alcohol'),
        ('flex', 'Flex'),
        ('electric', 'Eléctrico'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual','Manual'),
        ('automatic','Automática'),
    ]

    YEAR_CHOICES = [(year, year) for year in range(1886, date.today().year + 1)]


    # Unico de Motor
    brand = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Marca',
        max_length=255,
        min_length=1,
        required=True,
    )
    model = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Modelo',
        max_length=255,
        min_length=1,
        required=True,
    )
    fuel = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label = 'Combustible',
        choices=FUEL_CHOICES,
        required=True,
    )
    transmission = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Transmisión',
        choices=TRANSMISSION_CHOICES,
        required=True,
    )
    year = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Año',
        required=True,
        choices=YEAR_CHOICES,
        initial=date.today().year,
    )
    color = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
        label='Color',
        max_length=255,
        min_length=4,
        required=True,
    )

    #Compartido con BaseClass

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
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
        widget=forms.TextInput(attrs={'class':'form-control'}),
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
