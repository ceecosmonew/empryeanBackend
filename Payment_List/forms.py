from django import forms

from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ("name", "course_name", "amount", "email", "creditors_address", "phone", "message")
        