from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import EmpresaModel, FuncionarioModel, ClienteModel, AreaModel, ProdutoModel, MesaModel
from apps.usuarios.models import Perfil

from .forms import EmpresaForm, FuncionarioForm, ClienteForm, AreaForm, ProdutoForm, MesaForm
from django.db import models

# Create your views here.
def empresasView(request):
    contexto = {
        "empresas": EmpresaModel.objects.all()
    }
    return render(request, "empresas/empresasHome.html", contexto)

def empresasCadastrar(request):
    if(request.method == "POST"):
        formulario = EmpresaForm(request.POST)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("empresas:empresasHome")
    contexto = {
        "form": EmpresaForm()
    }
    return render(request, "empresas/empresasCadastrar.html", contexto)

def empresasEditar(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)
    if(request.method == "POST"):
        formulario = EmpresaForm(request.POST, instance = empresa)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("empresas:empresasHome")

    formulario = EmpresaForm(instance=empresa)
    contexto = {
        "form": formulario,
        "id": id,
    }
    return render(request, "empresas/empresasEditar.html", contexto)

def empresasDeletar(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)
    empresa.delete()
    return redirect("empresas:empresasHome")


def empresaOverview(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)
    contexto = {
        "id": id,
        "nome": empresa.nome,
        "data_cadastro": empresa.data_cadastro
    }

    return render(request, "empresas/empresaOverview.html", contexto)
from django.shortcuts import get_object_or_404

def funcionariosView(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)

    contexto = {
        "id": id,
        "funcionarios": empresa.funcionarios.all(),
        "empresa": empresa,
    }

    return render(request, "empresas/funcionario/empresasFuncionarios.html", contexto)

def funcionariosCadastrar(request, id):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # 1) cria login
            user = User.objects.create_user(
                username=username,
                password=password
            )

            # 2) cria funcionario sem salvar ainda
            funcionario = form.save(commit=False)
            funcionario.usuario = user
            funcionario.empresa_id = id
            funcionario.save()

            # 3) cria perfil
            Perfil.objects.create(
                user=user,
                role="funcionario"
            )

            return redirect("empresas:funcionarios", id=id)

    else:
        form = FuncionarioForm()

    contexto = {"form": form,
                "id": id}

    return render(request, "empresas/funcionario/empresasFuncionariosCadastrar.html", contexto)

def funcionariosEditar(request, id, idFunc):
    empresa = get_object_or_404(EmpresaModel, id=id)
    funcionario = get_object_or_404(FuncionarioModel, id = idFunc, empresa=empresa)

    if(request.method == "POST"):
        formulario = FuncionarioForm(request.POST, instance = funcionario)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("empresas:funcionarios", id=id)

    formulario = FuncionarioForm(instance=funcionario, modo="edicao")
    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/funcionario/empresasFuncionariosEditar.html", contexto)

def funcionariosDeletar(request, id, idFunc):
    empresa = get_object_or_404(EmpresaModel, id = id)
    funcionario = get_object_or_404(FuncionarioModel, id = idFunc, empresa=empresa)
    funcionario.delete()
    return redirect("empresas:funcionarios", id=id)

def clientesView(request, id):
    empresa = EmpresaModel.objects.get(id=id)
    contexto = {
        "id": id,
        "clientes": empresa.clientes.all()
    }
    return render(request, "empresas/clientes/empresasClientes.html", contexto)

def clientesCadastrar(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)
    if(request.method == "POST"):
        formulario = ClienteForm(request.POST)
        if(formulario.is_valid()):
            if not request.user.is_authenticated:
                return redirect('usuarios:login')
            cliente = formulario.save(commit=False)
            cliente.usuario = request.user
            cliente.empresa = empresa
            cliente.save()
            return redirect("empresas:clientes", id=id)
    else:
        formulario = ClienteForm()

    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/clientes/empresasClientesCadastrar.html", contexto)

def clientesEditar(request, id, idCliente):
    empresa = get_object_or_404(EmpresaModel, id=id)
    cliente = get_object_or_404(ClienteModel, id = idCliente, empresa=empresa)

    if(request.method == "POST"):
        formulario = ClienteForm(request.POST, instance = cliente)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("empresas:clientes", id=id)

    formulario = ClienteForm(instance=cliente)
    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/clientes/empresasClientesEditar.html", contexto)

def clientesDeletar(request, id, idCliente):
    empresa = get_object_or_404(EmpresaModel, id=id)
    cliente = get_object_or_404(ClienteModel, id = idCliente, empresa = empresa)
    cliente.delete()
    return redirect("empresas:clientes", id=id)


def produtosView(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)

    contexto = {
        "id": id,
        "produtos": empresa.produtos.all(),
        "empresa": empresa,
    }

    return render(request, "empresas/produtos/empresasProdutos.html", contexto)

def produtosCadastrar(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)
    if(request.method == "POST"):
        formulario = ProdutoForm(request.POST)
        if(formulario.is_valid()):
            if not request.user.is_authenticated:
                return redirect('usuarios:login')
            produto = formulario.save(commit=False)
            produto.usuario = request.user
            produto.empresa = empresa
            produto.save()
            return redirect("empresas:produtos", id=id)
    else:
        formulario = ProdutoForm()

    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/produtos/empresasProdutosCadastrar.html", contexto)

def produtosEditar(request, id, idProduto):
    empresa = get_object_or_404(EmpresaModel, id=id)
    produto = get_object_or_404(ProdutoModel, id = idProduto, empresa=empresa)

    if(request.method == "POST"):
        formulario = ProdutoForm(request.POST, instance = produto)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("empresas:produtos", id=id)

    formulario = ProdutoForm(instance=produto)
    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/produtos/empresasProdutosEditar.html", contexto)

def produtosDeletar(request, id, idProduto):
    empresa = get_object_or_404(EmpresaModel, id = id)
    produto = get_object_or_404(ProdutoModel, id = idProduto, empresa=empresa)
    produto.delete()
    return redirect("empresas:produtos", id=id)


def mesasView(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)

    contexto = {
        "id": id,
        "mesas": empresa.mesas.all(),
        "empresa": empresa,
    }

    return render(request, "empresas/mesas/empresasMesas.html", contexto)

def mesasCadastrar(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)
    if(request.method == "POST"):
        formulario = MesaForm(request.POST)
        if(formulario.is_valid()):
            if not request.user.is_authenticated:
                return redirect('usuarios:login')
            mesa = formulario.save(commit=False)
            mesa.usuario = request.user
            mesa.empresa = empresa
            mesa.save()
            return redirect("empresas:mesas", id=id)
    else:
        formulario = MesaForm()

    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/mesas/empresasMesasCadastrar.html", contexto)

def mesasEditar(request, id, idMesa):
    empresa = get_object_or_404(EmpresaModel, id=id)
    mesa = get_object_or_404(MesaModel, id = idMesa, empresa=empresa)

    if(request.method == "POST"):
        formulario = MesaForm(request.POST, instance = mesa)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("empresas:mesas", id=id)

    formulario = MesaForm(instance=mesa)
    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/mesas/empresasMesasEditar.html", contexto)

def mesasDeletar(request, id, idMesa):
    empresa = get_object_or_404(EmpresaModel, id=id)
    mesa = get_object_or_404(MesaModel, id = idMesa, empresa=empresa)
    mesa.delete()
    return redirect("empresas:mesas", id=id)

def areasView(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)

    contexto = {
        "id": id,
        "areas": empresa.areas.all(),
        "empresa": empresa,
    }

    return render(request, "empresas/areas/empresasAreas.html", contexto)

def areasCadastrar(request, id):
    empresa = get_object_or_404(EmpresaModel, id=id)
    if(request.method == "POST"):
        formulario = AreaForm(request.POST)
        if(formulario.is_valid()):
            if not request.user.is_authenticated:
                return redirect('usuarios:login')
            area = formulario.save(commit=False)
            area.usuario = request.user
            area.empresa = empresa
            area.save()
            return redirect("empresas:areas", id=id)
    else:
        formulario = AreaForm()

    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/areas/empresasAreasCadastrar.html", contexto)

def areasEditar(request, id, idArea):
    empresa = get_object_or_404(EmpresaModel, id=id)
    area = get_object_or_404(AreaModel, id = idArea, empresa=empresa)

    if(request.method == "POST"):
        formulario = AreaForm(request.POST, instance = area)
        if(formulario.is_valid()):
            formulario.save()
            return redirect("empresas:areas", id=id)

    formulario = AreaForm(instance=area)
    contexto = {
        "form": formulario,
        "empresa": empresa,
        "id": id
    }
    return render(request, "empresas/areas/empresasAreasEditar.html", contexto)

def areasDeletar(request, id, idArea):
    empresa = get_object_or_404(EmpresaModel, id = id)
    area = get_object_or_404(AreaModel, id = idArea, empresa=empresa)
    area.delete()
    return redirect("empresas:areas", id=id)
