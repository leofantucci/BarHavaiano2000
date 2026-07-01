from django.urls import path
from . import views

app_name = "empresas"

urlpatterns = [
    path("", views.empresasView, name="empresasHome"),
    path("cadastrar/", views.empresasCadastrar, name="empresasCadastrar"),
    path("editar/<int:id>", views.empresasEditar, name="empresasEditar"),
    path("deletar/<int:id>", views.empresasDeletar, name="empresasDeletar"),

    path("<int:id>/", views.empresaOverview, name="overview"),
    
    path("<int:id>/funcionarios/", views.funcionariosView, name="funcionarios"),
    path("<int:id>/funcionarios/cadastrar/", views.funcionariosCadastrar, name="funcionariosCadastrar"),
    path("<int:id>/funcionarios/editar/<int:idFunc>/", views.funcionariosEditar, name="funcionariosEditar"),
    path("<int:id>/funcionarios/deletar/<int:idFunc>/", views.funcionariosDeletar, name="funcionariosDeletar"),
    
    path("<int:id>/clientes/", views.clientesView, name="clientes"),
    path("<int:id>/clientes/cadastrar/", views.clientesCadastrar, name="clientesCadastrar"),
    path("<int:id>/clientes/editar/<int:idCliente>/", views.clientesEditar, name="clientesEditar"),
    path("<int:id>/clientes/deletar/<int:idCliente>/", views.clientesDeletar, name="clientesDeletar"),

    path("<int:id>/areas/", views.areasView, name="areas"),
    path("<int:id>/areas/cadastrar/", views.areasCadastrar, name="areasCadastrar"),
    path("<int:id>/areas/editar/<int:idArea>/", views.areasEditar, name="areasEditar"),
    path("<int:id>/areas/deletar/<int:idArea>/", views.areasDeletar, name="areasDeletar"),

    path("<int:id>/produtos/", views.produtosView, name="produtos"),
    path("<int:id>/produtos/cadastrar/", views.produtosCadastrar, name="produtosCadastrar"),
    path("<int:id>/produtos/editar/<int:idProduto>/", views.produtosEditar, name="produtosEditar"),
    path("<int:id>/produtos/deletar/<int:idProduto>/", views.produtosDeletar, name="produtosDeletar"),

    path("<int:id>/mesas/", views.mesasView, name="mesas"),
    path("<int:id>/mesas/cadastrar/", views.mesasCadastrar, name="mesasCadastrar"),
    path("<int:id>/mesas/editar/<int:idMesa>/", views.mesasEditar, name="mesasEditar"),
    path("<int:id>/mesas/deletar/<int:idMesa>/", views.mesasDeletar, name="mesasDeletar"),
]
