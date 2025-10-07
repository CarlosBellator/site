from django import forms
from django.contrib.auth.models import User

class CadastroForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}
        ),label='Senha'
    )
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}
        ),
        label='Confirmar Senha'
    )
    

    class Meta:
        model = User
        fields = ['first_name', 'email']
        labels = {
            'first_name': 'Nome',
            'email': 'Email',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}),
        }

    def clean_password_confirmation(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password != password_confirmation:
            raise forms.ValidationError("Digite a mesma senha nos dois campos")
        else:
            return password_confirmation

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Usar email como username
        user.set_password(self.cleaned_data['password_confirmation'])
        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}
        ), label='Email'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}
        ), label='Senha'
    )