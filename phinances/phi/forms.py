from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(label='Password', required=True, strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', required=True, strip=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username', 'password1', 'password2')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError(_("Password must be at least 8 characters long."))
        if not any(char.isupper() for char in password1):
            raise ValidationError(_("Password must contain at least one uppercase letter."))
        if not any(char.islower() for char in password1):
            raise ValidationError(_("Password must contain at least one lowercase letter."))
        if not any(char.isdigit() for char in password1):
            raise ValidationError(_("Password must contain at least one digit."))
        if all(char.isalnum() for char in password1):
            raise ValidationError(_("Password must contain at least one special character."))
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords do not match.')
        return password2
