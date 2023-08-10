from django import forms

class CadastrarCliente(forms.Form):
    sexo_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    nome = forms.CharField(max_length=50)
    endereco = forms.CharField(max_length=50)
    idade = forms.IntegerField()
    sexo = forms.ChoiceField(choices=sexo_choices)
    
    """
    exemplo de menssagem de erro
    data = forms.DateField(required=False, error_messages={'invalid': 'Data inválida'})
    """