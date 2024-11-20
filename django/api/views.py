from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .serializers import ClienteSerializer
from .forms import ClienteForm  # Importamos el nuevo forms.py


# ---------------- API ----------------
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genero', 'active', 'nivel_de_satisfaccion']


# ---------------- Templates ----------------
# Listar todos los clientes
def cliente_list(request):
    clientes = Cliente.objects.all()  # Consulta para obtener todos los clientes
    return render(request, 'clientes_templates/cliente_list.html', {'clientes': clientes})


# Crear un nuevo cliente
def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes_templates/cliente_form.html', {'form': form, 'title': 'Agregar Cliente'})


# Editar un cliente existente
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes_templates/cliente_form.html', {'form': form, 'title': 'Editar Cliente'})


# Eliminar un cliente
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes_templates/cliente_confirm_delete.html', {'cliente': cliente})
