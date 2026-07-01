from django.contrib import admin
from .models import *

admin.site.register(EmpresaModel)
admin.site.register(FuncionarioModel)
admin.site.register(ClienteModel)
admin.site.register(MesaModel)
admin.site.register(AreaModel)
admin.site.register(ProdutoModel)
admin.site.register(ComandaModel)
admin.site.register(PedidoModel)
admin.site.register(ItemPedidoModel)