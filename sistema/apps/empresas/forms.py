from django import forms
from .models import EmpresaModel, FuncionarioModel, ClienteModel, AreaModel, MesaModel, ProdutoModel

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = EmpresaModel
        fields = ['nome']


class FuncionarioForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = FuncionarioModel
        fields = [
            'nome',
            'cpf',
            'data_nascimento',
            'telefone',
            'cargo',
            'salario',
            'data_admissao',
            'data_demissao',
        ]

        widgets = {
                'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
                'data_admissao': forms.DateInput(attrs={'type': 'date'}),
                'data_demissao': forms.DateInput(attrs={'type': 'date'}),
            }

    def __init__(self, *args, modo="cadastro", **kwargs):
        super().__init__(*args, **kwargs)

        if modo == "edicao":
            self.fields.pop("username")
            self.fields.pop("password")
        if modo == "redefinir_senha":
            self.fields.pop("nome")
            self.fields.pop("cpf")
            self.fields.pop("data_nascimento")
            self.fields.pop("telefone")
            self.fields.pop("cargo")
            self.fields.pop("salario")
            self.fields.pop("data_admissao")
            self.fields.pop("data_demissao")
            self.fields.pop("username", None)
            self.fields["password"].label = "Nova senha"

class ClienteForm(forms.ModelForm):
    class Meta:
        model = ClienteModel
        fields = ['nome', 'telefone']

class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = ['nome', 'aberta']

class MesaForm(forms.ModelForm):
    class Meta:
        model = MesaModel
        fields = ['numero', 'qtd_lugares', 'disponivel']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = ProdutoModel
        fields = ['nome', 'area', 'preco', 'obs', 'qtd_estoque', 'disponivel']
