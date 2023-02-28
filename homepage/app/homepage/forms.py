from django import forms
from .models import DeliveryRequest


class DeliveryRequestForm(forms.ModelForm):
    class Meta:
        model = DeliveryRequest
        fields = [
            'loading_country',
            'loading_po_code',
            'requested_loading_date',
            'delivery_country',
            'delivery_po_code',
            'delivery_date',
            'ftl_ltl',
            'company_name',
            'pic_name',
            'phone_number',
        ]
