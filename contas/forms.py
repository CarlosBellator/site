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

class AlterarSenhaForm(forms.Form):
    senha_atual = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite sua senha atual'}
        ),
        label='Senha Atual',
        max_length=128
    )
    nova_senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite a nova senha'}
        ),
        label='Nova Senha',
        min_length=8,
        max_length=128,
        help_text='A senha deve ter pelo menos 8 caracteres.'
    )
    confirmar_nova_senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirme a nova senha'}
        ),
        label='Confirmar Nova Senha',
        max_length=128
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_senha_atual(self):
        senha_atual = self.cleaned_data.get('senha_atual')
        if not self.user.check_password(senha_atual):
            raise forms.ValidationError('Senha atual incorreta.')
        return senha_atual

    def clean_confirmar_nova_senha(self):
        nova_senha = self.cleaned_data.get('nova_senha')
        confirmar_nova_senha = self.cleaned_data.get('confirmar_nova_senha')
        
        if nova_senha and confirmar_nova_senha:
            if nova_senha != confirmar_nova_senha:
                raise forms.ValidationError('As senhas não coincidem.')
        return confirmar_nova_senha

    def clean_nova_senha(self):
        nova_senha = self.cleaned_data.get('nova_senha')
        
        # Validações de segurança da senha
        if nova_senha:
            # Verifica se tem pelo menos 8 caracteres
            if len(nova_senha) < 8:
                raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres.')
            
            # Verifica se não é muito simples
            if nova_senha.isdigit():
                raise forms.ValidationError('A senha não pode conter apenas números.')
                
            # Verifica se não é igual ao email do usuário
            if nova_senha.lower() == self.user.email.lower():
                raise forms.ValidationError('A senha não pode ser igual ao seu email.')
        
        return nova_senha

    def save(self):
        nova_senha = self.cleaned_data['nova_senha']
        self.user.set_password(nova_senha)
        self.user.save()
        return self.user