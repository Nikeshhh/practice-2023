from django import forms

from landing_backend.validators import telephone_validator


class WriteUsForm(forms.Form):

    fio = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'Input__inp',
                'type': 'text',
                'id': 'fio',
                'placeholder': 'ФИО'
            }
        )
    )

    tel = forms.CharField(
        max_length=18,
        required=True,
        validators=[telephone_validator],
        widget=forms.TextInput(
            attrs={
                'class': 'Input__inp',
                'type': 'tel',
                'id': 'tel',
                'placeholder': 'Телефон',
                'pattern': '[\+]\d{1}\s[\(]\d{3}[\)]\s\d{3}[\-]\d{2}[\-]\d{2}',
                'minlength': '18',
                'maxlength': '18',
            }
        )
    )

    email = forms.CharField(
        max_length=60,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'Input__inp',
                'type': 'email',
                'id': 'email',
                'placeholder': 'E-mail'
            }
        )
    )
