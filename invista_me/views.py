from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)


def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html', dados)

def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario) 

def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    # novo_investimento/1 -> GET
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html', {'formulario': formulario})
    # Caso requisicao seja POST
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')

def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == "POST":
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html', {'item': investimento})




def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')

def pagina_inicial(request):
    return HttpResponse('Pronto para comecar a inverstir')

def contato(request):
    return HttpResponse('Pagina de contato')

def minha_historia(request):
    pessoa = {
        'nome': 'Gabriel',
        'idade':22,
        'hobby': 'Prog'

    }
    return render(request, 'investimentos/minha_historia.html', pessoa)


def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento)



