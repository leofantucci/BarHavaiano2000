from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#EMPRESA#
class EmpresaModel(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    obs = models.TextField(max_length=255, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


#FUNCIONARIO#
class FuncionarioModel(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
        related_name="funcionarios"
    )
    cargo = models.CharField(max_length=255) 
    #cargo = models.ForeignKey(CargoModel, on_delete=models.CASCADE)
    data_nascimento = models.DateField(db_comment="Data de nasicmento do funcionário")
    telefone = models.CharField(max_length=11)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    contrato_ativo = models.BooleanField(default=True)
    data_admissao = models.DateField(db_comment="Data de admissão do funcionário")
    data_demissao = models.DateField(db_comment="Data de demissão do funcionário", null=True, blank=True)
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="funcionario"
    )

    def __str__(self):
        return self.nome

#CLIENTE#
class ClienteModel(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cliente"
    )
    empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
        related_name="clientes"
    )
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

#MESA#
class MesaModel(models.Model):
    empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
        related_name="mesas"
    )
    numero = models.IntegerField()
    qtd_lugares = models.IntegerField(default=4)
    disponivel = models.BooleanField(default=True)
    
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return Mesa + str(self.numero)

#COMANDA#
class ComandaModel(models.Model):
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(FuncionarioModel, on_delete=models.CASCADE)

    empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
        related_name="comandas"
    )
    mesa = models.ForeignKey(MesaModel, on_delete=models.CASCADE)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comanda {self.id}"


#PEDIDO#
class PedidoModel(models.Model):
    empresa = models.ForeignKey(
            EmpresaModel,
            on_delete=models.CASCADE,
            related_name="pedidos"
    )
    comanda = models.ForeignKey(ComandaModel, on_delete=models.CASCADE)
    entregue = models.BooleanField(default=False)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id}"

#AREA#
class AreaModel(models.Model):
    empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
        related_name="areas"
    )
    nome = models.CharField(max_length=255)
    aberta = models.BooleanField(default=True)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.nome

#PRODUTO#
class ProdutoModel(models.Model):
    empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
        related_name="produtos"
    )
    nome = models.CharField(max_length=255)
    area = models.ForeignKey(AreaModel, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    obs = models.TextField(max_length=255, blank=True)
    qtd_estoque = models.PositiveIntegerField()
    
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

#ITEM_PEDIDO#
class ItemPedidoModel(models.Model):
    empresa = models.ForeignKey(
        EmpresaModel,
        on_delete=models.CASCADE,
        related_name="itemPedidos"
    )
    pedido = models.ForeignKey(PedidoModel, on_delete=models.CASCADE)
    produto = models.ForeignKey(ProdutoModel, on_delete=models.CASCADE)
    preco_unit = models.DecimalField(max_digits=10, decimal_places=2)
    qtd = models.PositiveIntegerField(default=4)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Item_Pedido {self.id}"
