from django import forms
from .models import Register

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(forms.ModelForm):
    petition = forms.ChoiceField(
        choices=(('Paquete A', 'Paquete A'), ('Paquete B', 'Paquete B'), ('Paquete C', 'Paquete C')),
        widget=forms.Select(attrs={'class':'custom-select'}),
        error_messages={'invalid_choice': 'Seleccione un paquete'}
    )

    email = forms.EmailField(
        label='Correo',
        required=True,
        help_text='Introduzca un correo valido',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )

    date = forms.DateField(
        label='Fecha',
        widget=forms.DateInput(
            attrs={
            'id': 'id_date',
            'type': 'date',
            'class': 'form-control datetimepicker-input'
        }),
        help_text='Introduzca una fecha valida'
    )
        
    quantity = forms.IntegerField(
        label='Cantidad',
        min_value=1,
        error_messages={'min_value': 'Introduzca un numero'},
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'})
    )

    class Meta:
        widgets = {'date': DateInput()}
        model = Register
        fields = ('petition', 'email', 'date', 'quantity')