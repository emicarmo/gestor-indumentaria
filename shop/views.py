from django.shortcuts import render, redirect
from .models import Remera
from .forms import RemeraForm
from django.contrib import messages


def index(request):
    remeras = Remera.objects.all()
    messages.success(request, "¡Indumentaria listados!")
    datos = {"remeras": remeras}
    return render(request, "shop/index.html", datos)


def contacto(request):
    return render(request, "shop/contacto.html")

def nueva_remera(request, template_name='shop/nueva_remera.html'):
    if request.method == 'POST':
        form = RemeraForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "¡Indumentaria registrada!")
            return redirect("index")
    else:
        form = RemeraForm()
    dato = {
        'form': form
    }
    return render(request, template_name, dato)

def modificar_indumentaria(request, pk, template_name='shop/nueva_remera.html'):
    remera = Remera.objects.get(id=pk)
    form = RemeraForm(request.POST or None, instance=remera)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "¡Indumentaria actualizada!")
            return redirect('index')
    datos = {
        "form": form
    }
    return render(request, template_name, datos)

def eliminar_indumentaria(request, pk):
    remera = Remera.objects.get(id=pk)
    remera.delete()
    messages.success(request, "¡Indumentaria eliminada!")
    return redirect('index')