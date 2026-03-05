from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'office_company_name': forms.TextInput(attrs={'placeholder': 'Client Company Name...'}),
            'office_phone_number': forms.TextInput(attrs={'placeholder': 'Client Company Tel...'}),
            'office_address': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Client Company Address...'}),
            'work_description': forms.Textarea(attrs={'rows': 4}),
            'quantity': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        }
