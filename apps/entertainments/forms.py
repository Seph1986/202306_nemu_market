from django import forms

class EntertainmentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombre',
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
