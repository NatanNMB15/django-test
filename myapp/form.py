from django.forms import ModelForm, PasswordInput
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'dataCriacao', 'password']
        widgets = {
            'password': PasswordInput(),
        }