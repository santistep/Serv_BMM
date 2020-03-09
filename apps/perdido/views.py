from django.shortcuts import render, redirect

from apps.perdido.forms import PerdidoForm
from apps.perdido.models import Perdido

# Create your views here.


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response


def index(request):
    return render(request, 'perdido/index.html')


def perdido_view(request):
    if request.method == 'POST':
        form = PerdidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perdido:perdido_listar')
    else:
        form = PerdidoForm()
    return render(request, 'perdido/perdido_form.html', {'form': form})


def perdido_list(request):
    perdido = Perdido.objects.all().order_by('id')
    contexto = {'perdidos': perdido}
    return render(request, 'perdido/perdido_list.html', contexto)


def perdido_edit(request, id_perdido):
    perdido = Perdido.objects.get(id=id_perdido)
    if request.method == 'GET':
        form = PerdidoForm(instance=perdido)
    else:
        form = Perdido(request.POST, instance=perdido)
        if form.is_valid():
            form.save()
        return redirect(perdido_list)
    return render(request, 'perdido/perdido_form.html', {'form': form})


def perdido_delete(request, id_perdido):
    perdido = Perdido.objects.get(id=id_perdido)
    if request.method == 'POST':
        perdido.delete()
        return redirect(perdido_list)
    return render(request, 'perdido/perdido_delete.html', {'perdido': perdido})
