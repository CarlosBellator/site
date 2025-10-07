from django.shortcuts import redirect, render
from contas.forms import CadastroForm, LoginForm

from django.contrib import auth , messages
# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form['email'].value()
            password = form['password'].value()
            print(f'Email: {email} - Senha: {password}')
            usuario = auth.authenticate(
                request,
                username=email,
                password=password)
            if usuario is not None:
                auth.login(request, usuario)
                print('Usuário logado com sucesso')
                messages.success(request, f'Bem vindo {email}!')
                return redirect('home')
            else:
                print('Senha incorreta')
                messages.error(request, 'Senha incorreta')
                return redirect('login')
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    is_mobile = any(device in user_agent for device in ['mobile', 'android', 'iphone'])
    if is_mobile:
        return render(request, 'contas/login-mobile.html', {'form': form})
    else:
        return render(request, 'contas/login-desktop.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')

def cadastro(request):
    form = CadastroForm()
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    is_mobile = any(device in user_agent for device in ['mobile', 'android', 'iphone'])
    if is_mobile:
        return render(request, 'contas/cadastro-mobile.html', {'form': form})
    else:
        return render(request, 'contas/cadastro-desktop.html', {'form': form})