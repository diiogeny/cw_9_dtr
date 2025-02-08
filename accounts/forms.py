from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        import re
        pattern = r'^\+996 \d{3} \d{3} \d{3}$'
        if not re.match(pattern, phone):
            raise forms.ValidationError("Номер телефона должен быть в формате +996 XXX XXX XXX")
        return phone


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone"]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password']


