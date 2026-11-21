from django import forms
from django.core.validators import RegexValidator

from .models import ContactMessage


phone_validator = RegexValidator(r"^[+\d][\d\s()-]{6,29}$", "Enter a valid phone number.")


class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=False, validators=[phone_validator], widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone number (optional)"}))

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email address", "autocomplete": "email"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Tell us about your custom gift", "rows": 5}),
        }

    def clean_name(self):
        return " ".join(self.cleaned_data["name"].split())

    def clean_message(self):
        message = " ".join(self.cleaned_data["message"].split())
        if len(message) < 10:
            raise forms.ValidationError("Please provide a little more detail (at least 10 characters).")
        return message
