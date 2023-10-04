from django import forms


class ElectronicForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Título',
        max_length=255,
        min_length=1,
        required=True,
    )

    price = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Precio',
        min_value=1,
        required=True,
        error_messages={
            'invalid': 'Por favor, ingrese un número válido para el precio.',
        }

    )

    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Ubicación',
        max_length=255,
        min_length=4,
        required=True,
    )

    phone1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Celular 1',
        min_length=8,
        required=True,
        error_messages={
            'invalid': 'Por favor, ingrese un número de contacto válido',
        }

    )

    phone2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Celular 2',
        min_length=8,
        required=False
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Email',
        error_messages={
            'invalid': 'Por favor, ingrese un email válido.',
        }

    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Descripción',
        max_length=255,
        min_length=1,
        required=True,
    )
