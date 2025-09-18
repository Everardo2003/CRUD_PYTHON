from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario

# Lista de usuarios
def lista(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

# Crear usuario
def crear(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/formulario.html', {'form': form})

# Editar usuario
def editar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/formulario.html', {'form': form})

# Eliminar usuario
def eliminar(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista')
    return render(request, 'usuarios/eliminar.html', {'usuario': usuario})
