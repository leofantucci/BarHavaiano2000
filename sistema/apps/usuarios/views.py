from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm

from django.shortcuts import render, redirect
from .models import Perfil
from .forms import UserForm

def registerView(request, role):

    # segurança básica (evita qualquer valor inválido)
    roles_validas = ['cliente', 'funcionario', 'gerente']
    if role not in roles_validas:
        return redirect('register', role='cliente')

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Perfil.objects.create(
                user=user,
                role=role
            )

            return redirect('usuarios:login')

    else:
        form = UserForm()

    return render(request, 'usuarios/register.html', {
        'form': form,
        'role': role
    })

def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'usuarios/login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'usuarios/login.html')

def logoutView(request):
    logout(request)
    return redirect('usuarios:login')


def usuariosView(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)

    usuarios = User.objects.select_related('perfil').filter(
        perfil__empresa=empresa
    )

    return render(request, 'usuarios/usuariosView.html', {
        'usuarios': usuarios,
        'empresa': empresa
    })
