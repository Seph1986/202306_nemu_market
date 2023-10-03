from django import forms

from datetime import date


class MotorForm(forms.Form):
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
    )