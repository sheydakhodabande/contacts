from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone_number',
        ]

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تلفن',
        }

        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'phone_number': forms.TextInput(),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']

        if not phone.isdigit():
            raise forms.ValidationError(
        'شماره تلفن باید فقط شامل اعداد باشد.'
    )

        if len(phone) != 11:
            raise forms.ValidationError(
        'شماره تلفن باید ۱۱ رقم باشد.'
    )

        if not phone.startswith('09'):
            raise forms.ValidationError(
        'شماره تلفن باید با 09 شروع شود.'
        )

        return phone
