from django.shortcuts import render
from .forms import CadastrarCliente
from .models import Cliente


def cadastro(request):
    if request.method == 'GET':
        form = CadastrarCliente()

        return render(request, 'cadastro.html', {'form': form})
    else:
        message = ''
        form = CadastrarCliente(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                cliente = Cliente(
                    nome = data['nome'],
                    endereco = data['endereco'],
                    idade = data['idade'],
                    sexo = data['sexo']
                    )
                
                print(cliente)

                cliente.save()

                message = 'Deu certo'

                form = CadastrarCliente()

            except (NameError) :
                message = 'Deu erro'
                print(NameError)


        else:
            pass
        return render(request, 'cadastro.html', {'form': form, 'message': message})


def listar_clientes(request):
    clientes = Cliente.objects.all()

    return render(request, 'listar_clientes.html', {'clientes': clientes})